import os


def swap(srcFile, tempFile, dstFile):

    try:
        os.rename(dstFile, tempFile)
    except Exception as e:
        print(e)
        print('rename file fail\r\n')
    else:
        print('rename file success\r\n')

    try:
        os.rename(srcFile, dstFile)
    except Exception as e:
        print(e)
        print('rename file fail\r\n')
    else:
        print('rename file success\r\n')

    try:
        os.rename(tempFile, srcFile)
    except Exception as e:
        print(e)
        print('rename file fail\r\n')
    else:
        print('rename file success\r\n')


