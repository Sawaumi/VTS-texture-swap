import os
import json

import asyncio
import websockets

import func
from func import *
from util import *

try:
    import winreg
except Exception as e_import_winreg:
    print(e_import_winreg)

"""
Huge thanks to emlo40's frame work: https://github.com/mlo40/VsPyYt
"""

motions = ["motions/removeHair.exp3.json",
           "motions/tintTexture.exp3.json",
           "motions/textureSwap.exp3.json"]


async def setup(ws):
    if os.path.exists('token.json'):
        print('Loading authtoken From File...')
        with open('token.json', "r") as json_file:
            data = json.load(json_file)
            auth_token = (data['authenticationkey'])
            confirm = await authorize(ws, auth_token)
            if auth_token == "" or not confirm["data"]["authenticated"]:
                print('Error Token Invalid')
                print('Fetching New Tokens...')
                auth_token = await get_auth_token(ws)
                print(auth_token)
                print('Saving authtoken for Future Use...')
                data["authenticationkey"] = auth_token
                json_file.close()
                json_file = open('token.json', "w")
                json_file.write(json.dumps(data))
                json_file.close()
                print("Saving finished")
            else:
                json_file.close()
    else:
        print('Fetching New Tokens...')
        auth_token = await get_auth_token(ws)
        print(auth_token)
        print('Saving authtoken for Future Use...')
        with open('token.json', "w") as json_file:
            json_file_con = {
                "chatspeed": 0.1,
                "authenticationkey": auth_token,
                "authenticationkeytwitch": ""
            }
            json_file.write(json.dumps(json_file_con))
            json_file.close()
        await authorize(ws, auth_token)

    if os.path.exists('path.json'):
        print('Loading texture path From File...')
        # with open('path.json', "r") as json_file:
        #     data = json.load(json_file)
        #     base_path = data["basePath"]
        #     json_file.close()
        # os.chdir(base_path)
    else:
        print('Fetching texture path...')
        try:
            access_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                        r"SOFTWARE\Microsoft\Windows\CurrentVersion"
                                        r"\Uninstall")
            sub_key = winreg.OpenKey(access_key, "Steam App 1325860",
                                     0, winreg.KEY_ALL_ACCESS)
            base_path = winreg.QueryValueEx(sub_key, "InstallLocation")[0]
            print(base_path)

            ''' 
            should request VTS for the name of "Live2DModels" since 
            A. it can be done so
            B. Not have to change it if the name changes
            '''
            base_path += r"\VTube Studio_Data\StreamingAssets\Live2DModels"
            print(base_path)

            curr_model = (await get_curr_model(ws))["data"]
            vts_model_name = curr_model["vtsModelName"]

            if vts_model_name == "":
                print("No model has been loaded")
            else:
                model_folder_path = get_file_path(root_path=base_path,
                                                  file_name=vts_model_name)[1]
                model_folder_path = model_folder_path.replace('\\', '/') + '/'

                json_path = model_folder_path + curr_model["live2DModelName"]
                model_json = open(json_path, mode='r', buffering=-1).read()
                model_json = json.loads(model_json)

                textures = model_json["FileReferences"]["Textures"]
                '''
                model_folder_path + [texture in textures] = src_path
                replace .png -> swap.png = dst_path
                replace .png -> temp.png = temp_path
                '''
                print('Saving path for future Use...')
                with open('path.json', "w") as json_file:
                    json_file_con = {
                        "basePath": model_folder_path,
                        "textureArray": textures
                    }
                    json_file.write(json.dumps(json_file_con))
                    json_file.close()
                # print('Path saved, please restart the plugin')

        except Exception as e_get_key:
            print(e_get_key)

    print('Checking exp3 files...')
    with open('path.json', "r") as json_file:
        data = json.load(json_file)
        base_path = data["basePath"]
        json_file.close()
    # remove_hair_exp = (base_path + motions[0])
    # print(remove_hair_exp)
    motion_found = True
    for motion in motions:
        motion_path = base_path + motion
        if not os.path.exists(motion_path):
            motion_found = False
            print(motion, "not exist, creating file...")
            with open(motion_path, "w") as json_file:
                json_file_con = {
                    "Type": "Live2D Expression",
                    "Parameters": []
                }
                json_file.write(json.dumps(json_file_con))
                json_file.close()
    if motion_found:
        print("All exp3 files found, please bind as your need")
    # load token
    with open('token.json') as json_file:
        data = json.load(json_file)
        json_file.close()
    print("Successfully Loaded")
