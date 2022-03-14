import os
import json
import configparser

import asyncio
import websockets

import func
from func import *


async def setup(ws):
    if os.path.exists('token.json'):
        print('Loading authtoken From File...')
        with open('token.json', "r") as json_file:
            data = json.load(json_file)
            auth_token = (data['authenticationkey'])
            confirm = await authorize(ws, auth_token)
            if auth_token == "" or confirm["data"]["authenticated"] == False:
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

    with open('token.json') as json_file:
        data = json.load(json_file)
        json_file.close()
    print("Successfully Loaded")

