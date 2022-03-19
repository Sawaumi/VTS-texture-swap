import setup
from setup import *
import websockets
from func import *
from util import *


# from nameSwap import swap


async def main():
    # async with websockets.connect('ws://127.0.0.1:8001') as ws:
    try:
        ws = await websockets.connect('ws://127.0.0.1:8001')
    except Exception as e:
        print("Couldn't connect to VtubeStudio")
        print(e)
        input("press enter to quit program")
        quit()
    await setup(ws)

    with open('path.json', "r") as json_file:
        data = json.load(json_file)
        base_path = data["basePath"]
        textures = data["textureArray"]
        src_path, dst_path, temp_path = [], [], []
        for texture in textures:
            src_path.append(base_path + texture)
            dst_path.append(base_path + texture.replace('.png', '_swap.png'))
            temp_path.append(base_path + texture.replace('.png', '_temp.png'))
        json_file.close()

    # abs_path = path.replace('\\', '/') + '/'
    #
    # src_file = abs_path + src_file_name
    # temp_file = abs_path + temp_file_name
    # dst_file = abs_path + dst_file_name

    # task_idle_trigger = asyncio.create_task(idle_sequence(ws))
    # task_remove_hair_trigger = asyncio.create_task(remove_hair_sequence(ws))
    # task_texture_swap_trigger = asyncio.create_task(texture_swap_sequence(ws, src_file, temp_file, dst_file))
    # 
    # await task_idle_trigger
    # await task_remove_hair_trigger
    # await task_texture_swap_trigger
    # 
    # await asyncio.gather(idle_sequence(ws),
    #                      remove_hair_sequence(ws),texture_swap_sequence(ws, src_file, temp_file, dst_file))

    # print(await get_model_art_mesh_list(ws))

    await exec_hotkey(ws, "ResetAllExpressions")
    swapped = await if_exp_active(ws, "textureSwap.exp3.json")
    texture_idled = True
    hair_lost = False

    while True:
        # Swap texture
        swap_trigger = await if_exp_active(ws, "textureSwap.exp3.json")
        if swap_trigger ^ swapped:
            await swap_texture(ws, src_path, dst_path, temp_path)
            swapped ^= True

        # idle animation
        face_is_found = await if_face_found(ws)
        # Uncomment next line to bypass this feature
        face_is_found = True
        texture_idled = await idle_texture(ws, face_is_found, texture_idled)
        # if face_is_found and not in_idle:
        #     print("back from idle")
        #     await fade_back(ws, if_tint_all=True)
        #     in_idle = True
        #
        # elif not face_is_found and in_idle:
        #     print("gone idle")
        #     await fade_away(ws, if_tint_all=True)
        #     in_idle = False

        # Toggle hair
        hair_loss_triggered = await if_exp_active(ws, "removeHair.exp3.json")
        hair_lost = await hair_loss(ws, hair_loss_triggered, hair_lost)
        # if hair_loss_triggered and not hair_loss_toggle:
        #     print("removed hair")
        #     await fade_away(ws, con_array=["ce", "fa", "qian", "hfa", "tding", "ying"])
        #     hair_loss_toggle = True
        #
        # elif not hair_loss_triggered and hair_loss_toggle:
        #     print("added hair")
        #     await fade_back(ws, con_array=["ce", "fa", "qian", "hfa", "tding", "ying"])
        #     hair_loss_toggle = False

        # bottom of main loop
        await asyncio.sleep(0.03)


asyncio.run(main())
