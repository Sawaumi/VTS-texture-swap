import asyncio
from os import system, name
import json

from util import *

######################################
#          plugin settings           #
######################################
dev = "Sawaumi"
request_id = "VtextureSwap_v0.2.0 "
plugin_name = "VtextureSwap"
api_version = "1.0"


######################################
#             functions              #
######################################
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


async def get_auth_token(ws):
    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": api_version,
        "requestID": request_id,
        "messageType": "AuthenticationTokenRequest",
        "data": {
            "pluginName": plugin_name,
            "pluginDeveloper": dev,
        }
    }
    await ws.send(json.dumps(payload))
    json_data = await ws.recv()
    pack = json.loads(json_data)
    auth_token = pack['data']['authenticationToken']
    return auth_token


async def authorize(ws, auth_token):
    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": api_version,
        "requestID": request_id,
        "messageType": "AuthenticationRequest",
        "data": {
            "pluginName": plugin_name,
            "pluginDeveloper": dev,
            "authenticationToken": auth_token
        }
    }
    await ws.send(json.dumps(payload))
    json_data = await ws.recv()
    pack = json.loads(json_data)
    return pack


async def get_param_list(ws):
    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": api_version,
        "requestID": request_id,
        "messageType": "InputParameterListRequest"
    }
    await ws.send(json.dumps(payload))
    json_data = await ws.recv()
    pack = json.loads(json_data)
    return pack


async def create_param(ws, parameterName, lower_bound, upper_bound, defaultValue, explanation):
    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": api_version,
        "requestID": "SomeID",
        "messageType": "ParameterCreationRequest",
        "data": {
            "parameterName": parameterName,
            "explanation": explanation,
            "min": lower_bound,
            "max": upper_bound,
            "defaultValue": defaultValue
        }
    }
    await ws.send(json.dumps(payload))
    json_data = await ws.recv()
    pack = json.loads(json_data)
    return pack


async def get_param_value(ws, param):
    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": api_version,
        "requestID": "SomeID",
        "messageType": "ParameterValueRequest",
        "data": {
            "name": param
        }
    }
    await ws.send(json.dumps(payload))
    json_data = await ws.recv()
    pack = json.loads(json_data)
    return pack


async def set_param_value(ws, param, value):
    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": api_version,
        "requestID": "SomeID",
        "messageType": "InjectParameterDataRequest",
        "data": {
            "parameterValues": [
                {
                    "id": param,
                    "value": value
                }
            ]
        }
    }
    await ws.send(json.dumps(payload))
    json_data = await ws.recv()
    pack = json.loads(json_data)
    return pack


async def get_curr_model(ws):
    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": api_version,
        "requestID": request_id,
        "messageType": "CurrentModelRequest"
    }
    await ws.send(json.dumps(payload))
    json_data = await ws.recv()
    pack = json.loads(json_data)
    return pack


async def list_avail_model(ws):
    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": api_version,
        "requestID": request_id,
        "messageType": "AvailableModelsRequest"
    }
    await ws.send(json.dumps(payload))
    json_data = await ws.recv()
    pack = json.loads(json_data)
    return pack


async def get_api_state(ws):
    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": api_version,
        "requestID": request_id,
        "messageType": "APIStateRequest",
    }
    await ws.send(json.dumps(payload))
    json_data = await ws.recv()
    pack = json.loads(json_data)
    return pack


async def get_states(ws):
    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": api_version,
        "requestID": request_id,
        "messageType": "StatisticsRequest"
    }
    await ws.send(json.dumps(payload))
    json_data = await ws.recv()
    pack = json.loads(json_data)
    return pack


async def if_face_found(ws):
    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": "1.0",
        "requestID": "SomeID",
        "messageType": "FaceFoundRequest"
    }
    await ws.send(json.dumps(payload))
    json_data = await ws.recv()
    pack = json.loads(json_data)
    try:
        data = pack["data"]["found"]
        return data
    except KeyError:
        print(pack)
    # return pack["data"]["found"]


async def get_vts_folder_info(ws):
    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": api_version,
        "requestID": request_id,
        "messageType": "VTSFolderInfoRequest"
    }
    await ws.send(json.dumps(payload))
    json_data = await ws.recv()
    pack = json.loads(json_data)
    # authres = pack['data']
    # what was this for?
    return pack


async def get_curr_hotkeys(ws, model_id):
    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": api_version,
        "requestID": request_id,
        "messageType": "HotkeysInCurrentModelRequest",
        "data": {
            "modelID": model_id,
        }
    }
    await ws.send(json.dumps(payload))
    json_data = await ws.recv()
    pack = json.loads(json_data)
    return pack


async def exec_hotkey(ws, hotkey_id):
    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": api_version,
        "requestID": request_id,
        "messageType": "HotkeyTriggerRequest",
        "data": {
            "hotkeyID": hotkey_id
        }
    }
    await ws.send(json.dumps(payload))
    json_data = await ws.recv()
    pack = json.loads(json_data)
    return pack


# async def force_exec_hotkey(websocket, hkid):
#     payload = {
#         "apiName": "VTubeStudioPublicAPI",
#         "apiVersion": api_version,
#         "requestID": request_id,
#         "messageType": "HotkeyTriggerRequest",
#         "data": {
#             "hotkeyID": hkid
#         }
#     }
#     await websocket.send(json.dumps(payload))
#     return


async def get_exp_state(ws, exp_file_name, if_include_detail=False):
    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": api_version,
        "requestID": request_id,
        "messageType": "ExpressionStateRequest",
        "data": {
            "details": if_include_detail,
            "expressionFile": exp_file_name,
        }
    }
    await ws.send(json.dumps(payload))
    json_data = await ws.recv()
    pack = json.loads(json_data)
    return pack


async def if_exp_active(ws, exp_file_name):
    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": api_version,
        "requestID": request_id,
        "messageType": "ExpressionStateRequest",
        "data": {
            "details": False,
            "expressionFile": exp_file_name,
        }
    }
    await ws.send(json.dumps(payload))
    # logging.info("calling recv", exc_info=True)
    json_data = await ws.recv()
    pack = json.loads(json_data)
    try:
        data = pack["data"]["expressions"][0]["active"]
        return data
    except KeyError:
        print(pack)
    # return pack["data"]["expressions"][0]["active"]


async def load_model(ws, model_id):
    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": api_version,
        "requestID": request_id,
        "messageType": "ModelLoadRequest",
        "data": {
            "modelID": model_id
        }
    }
    await ws.send(json.dumps(payload))
    json_data = await ws.recv()
    pack = json.loads(json_data)
    return pack


async def move_model(ws, t, relativity, x, y, rot, size):
    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": api_version,
        "requestID": request_id,
        "messageType": "MoveModelRequest",
        "data": {
            "timeInSeconds": t,
            "valuesAreRelativeToModel": relativity,
            "positionX": x,
            "positionY": y,
            "rotation": rot,
            "size": size
        }
    }
    await ws.send(json.dumps(payload))
    json_data = await ws.recv()
    pack = json.loads(json_data)
    return pack


async def get_model_art_mesh_list(ws):
    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": api_version,
        "requestID": request_id,
        "messageType": "ArtMeshListRequest"
    }
    await ws.send(json.dumps(payload))
    json_data = await ws.recv()
    pack = json.loads(json_data)
    return pack


async def tint_art_mesh(ws, r=255, g=255, b=255, a=255,
                        if_tint_all=False, enable_rainbow=False,
                        if_mix_with_scene_lighting=True,
                        art_mesh_number="",
                        exact_array="", con_array="",
                        tag_exact_array="", tag_contain_array=""):
    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": api_version,
        "requestID": request_id,
        "messageType": "ColorTintRequest",
        "data": {
            "colorTint": {
                "colorR": r,
                "colorG": g,
                "colorB": b,
                "colorA": a,
                "mixWithSceneLightingColor": if_mix_with_scene_lighting,
                "jeb_": enable_rainbow
            },
            "artMeshMatcher": {
                "tintAll": if_tint_all,
                "artMeshNumber": art_mesh_number,
                "nameExact": exact_array,
                "nameContains": con_array,
                "tagExact": tag_exact_array,
                "tagContains": tag_contain_array
            }
        }
    }
    await ws.send(json.dumps(payload))
    json_data = await ws.recv()
    pack = json.loads(json_data)
    return pack


async def spin(ws, x, y, s):
    await move_model(ws, 0.2, False, x, y, 90, s)
    await asyncio.sleep(0.1)
    await move_model(ws, 0.2, False, x, y, 180, s)
    await asyncio.sleep(0.1)
    await move_model(ws, 0.2, False, x, y, 270, s)
    await asyncio.sleep(0.1)
    await move_model(ws, 0.2, False, x, y, 360, s)
    await asyncio.sleep(0.1)


async def fade_away(ws, if_tint_all=False, con_array=None):
    if con_array is None:
        con_array = [""]
    for i in range(16):
        await tint_art_mesh(ws, a=255 - i * 17, if_tint_all=if_tint_all, con_array=con_array)
        await asyncio.sleep(0.02)
    # print("faded away")
    # print(con_array)


async def fade_back(ws, if_tint_all=False, con_array=None):
    if con_array is None:
        con_array = [""]
    for i in range(16):
        await tint_art_mesh(ws, a=i * 17, if_tint_all=if_tint_all, con_array=con_array)
        await asyncio.sleep(0.02)
    # print("faded back")
    # print(con_array)


async def swap_texture(ws, src_path, dst_path, temp_path):
    for src, dst, temp in zip(src_path, dst_path, temp_path):
        swap(src, dst, temp)
    await asyncio.sleep(2)
    await exec_hotkey(ws, "ReloadModelTexture")
    print("texture_swapped")


async def swap_debug(ws, src_path, dst_path, temp_path):
    for src, dst, temp in zip(src_path, dst_path, temp_path):
        print(src, dst, temp)


async def idle_texture(ws, face_is_found, texture_idled):
    if face_is_found and not texture_idled:
        print("back from idle")
        await fade_back(ws, if_tint_all=True)
        texture_idled = True

    elif not face_is_found and texture_idled:
        print("gone idle")
        await fade_away(ws, if_tint_all=True)
        texture_idled = False
    return texture_idled


async def hair_loss(ws, hair_loss_triggered, hair_loss_toggle):
    if hair_loss_triggered and not hair_loss_toggle:
        print("removed hair")
        await fade_away(ws, con_array=["ce", "fa", "qian", "hfa", "tding", "ying"])
        hair_loss_toggle = True

    elif not hair_loss_triggered and hair_loss_toggle:
        print("added hair")
        await fade_back(ws, con_array=["ce", "fa", "qian", "hfa", "tding", "ying"])
        hair_loss_toggle = False
    return hair_loss_toggle

