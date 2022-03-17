import json
import time
import os

import setup
from setup import *

from nameSwap import swap

###########################################
#          texture path settings          #
###########################################
# Please replace content in <> 
# with the absolute path for the texture folder in your model directory
# e.g:
# path = r'G:\SteamLibrary\steamapps\common\VTube Studio\VTube Studio_Data\StreamingAssets\Live2DModels\juzi_1123\juzi.4096'
path = r'<Absolute path for the texture folder in your model directory>'

# default = 'texture_00.png'
src_file_name = 'texture_00.png'

# default = 'texture_00_swap.png'
dst_file_name = 'texture_00_swap.png'

# Swap is done by src->temp, dst->src, temp->dst
# default = 'texture_00_temp.png'
temp_file_name = 'texture_00_temp.png'
# ======================================


async def main():
    try:
        ws = await websockets.connect('ws://127.0.0.1:8001')
    except:
        print("Couldn't connect to vtube studio")
        input("press enter to quit program")
        quit()
    await setup(ws)

    abs_path = path.replace('\\', '/') + '/'

    src_file = abs_path + src_file_name
    temp_file = abs_path + temp_file_name
    dst_file = abs_path + dst_file_name

    while True:
        trigger = await get_exp_state(ws, "textureSwap.exp3.json", True)
        trigger = trigger["data"]["expressions"][0]["active"]
        while trigger:
            print("triggered")
            swap(src_file, temp_file, dst_file)
            trigger = False
            time.sleep(1.3)
            await exec_hotkey(ws, "ReloadModelTexture")
        time.sleep(0.03)


asyncio.run(main())
