from os import system, name
import json
import time

######################################
#          plugin settings           #
######################################
dev = "Sawaumi"
request_id = "VtextureSwap_v0.1.1 "
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


async def get_exp_state(ws, exp_file_name, if_include_detail, ):
    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": api_version,
        "requestID": "SomeID",
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


async def get_art_mesh(ws):
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


async def tint_art_mesh(ws, r, g, b, a, tint_all, num, exact_array, con_array, tag_exact_array, tag_contain_array):
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
                "colorA": a
            },
            "artMeshMatcher": {
                "tintAll": tint_all,
                "artMeshNumber": num,
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
    time.sleep(0.1)
    await move_model(ws, 0.2, False, x, y, 180, s)
    time.sleep(0.1)
    await move_model(ws, 0.2, False, x, y, 270, s)
    time.sleep(0.1)
    await move_model(ws, 0.2, False, x, y, 360, s)
    time.sleep(0.1)


async def rainbow(ws):
    await tint_art_mesh(ws, 255, 0, 0, 255, True, "", "", "", "", "")
    time.sleep(0.03)
    await tint_art_mesh(ws, 255, 127, 0, 255, True, "", "", "", "", "")
    time.sleep(0.03)
    await tint_art_mesh(ws, 255, 255, 0, 255, True, "", "", "", "", "")
    time.sleep(0.03)
    await tint_art_mesh(ws, 0, 255, 0, 255, True, "", "", "", "", "")
    time.sleep(0.03)
    await tint_art_mesh(ws, 0, 0, 255, 255, True, "", "", "", "", "")
    time.sleep(0.03)
    await tint_art_mesh(ws, 46, 43, 95, 255, True, "", "", "", "", "")
    time.sleep(0.03)
    await tint_art_mesh(ws, 139, 0, 255, 255, True, "", "", "", "", "")
    time.sleep(0.03)
    await tint_art_mesh(ws, 255, 255, 255, 255, True, "", "", "", "", "")
