import os
from os.path import isfile
from os.path import join

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
abs_path_default = path.replace('\\', '/') + '/'
src_path_default = abs_path_default + src_file_name
temp_path_default = abs_path_default + temp_file_name
dst_path_default = abs_path_default + dst_file_name


# ======================================


def swap(srcFile=src_path_default, dstFile=dst_path_default, tempFile=temp_path_default, if_default=False):
    if if_default:
        swap()
    else:
        if os.path.exists(srcFile) and os.path.exists(dstFile):
            try:
                os.rename(dstFile, tempFile)
            except Exception as e:
                print(e)
            # else:
            #     print('rename file success\r\n')

            try:
                os.rename(srcFile, dstFile)
            except Exception as e:
                print(e)
            # else:
            #     print('rename file success\r\n')

            try:
                os.rename(tempFile, srcFile)
            except Exception as e:
                print(e)
            # else:
            #     print('rename file success\r\n')
            # print("SWAPPPPP")
        else:
            print("not found")
            # print(srcFile, tempFile, dstFile)


def get_file_path(root_path, file_name, depth=1):
    # print blue("当前查找目录：{}，递归层级：{}".format(filepath, find_depth))
    # 递归深度控制
    for file_ in os.listdir(root_path):
        # print cyan("file: {}".format(file_))
        if isfile(join(root_path, file_)):
            # print "当前文件：{}".format(file_)
            if file_ == file_name:
                return True, root_path
        elif depth <= 0:  # 递归深度控制, 为0时退出
            continue
        else:
            result, abs_path = get_file_path(root_path=join(root_path, file_),
                                             file_name=file_name)
            if result:
                print("File \"{}\" found at {}".format(file_name, abs_path))
                return result, abs_path
    return False, root_path
