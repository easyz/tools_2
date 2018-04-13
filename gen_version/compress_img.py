#coding:utf8

import os  
import os.path  
import PIL.Image as Image
import shutil
  
WORK = os.path.dirname(__file__)

pngquantPath = os.path.join(WORK, "libs\\pngquant\\pngquant.exe -f --ext .c_png --quality 40-90 ")
pngquant2Path = os.path.join(WORK, "libs\\pngquant\\pngquant.exe -f --ext .png --quality 40-90 ")

# def GetConfigFile(filePath):
#     if filePath.endswith(".png")

def Compress(root, imageDir, outdir, copyJson = False):
    pngFile = []
    copyFile = []
    print("=> check dir " + os.path.join(root, imageDir))
    for parent, dirnames, filenames in os.walk(os.path.join(root, imageDir)):
        for filename in filenames:
            path = os.path.join(parent, filename)
            newPath = path.replace(root, outdir)
            if not os.path.exists(os.path.dirname(newPath)):
                print(os.path.dirname(newPath))
                os.makedirs(os.path.dirname(newPath))
            shutil.copy(path, newPath)
            print("=> copy " + path)
            if not path.endswith(".png"):
                continue
            im = Image.open(newPath)
            isP = im.mode != "P"
            im.close()
            if isP:
                print("=> compress " + newPath)
                os.system(pngquant2Path + "\"" + newPath + "\"")
    """
    for parent, dirnames, filenames in os.walk(os.path.join(root, imageDir)):
        for filename in filenames:
            if filename.find(".png") == -1:
                continue
            path = os.path.join(parent, filename)
            im = Image.open(path)
            if im.mode != "P":
                pngFile.append(path)
            else:
                copyFile.append(path)

    for filename in pngFile:
        os.system(pngquantPath + "\"" + filename + "\"")
        inPath = filename.replace(".png", ".c_png")
        newPath = filename.replace(root, outdir)
        if not os.path.exists(os.path.dirname(newPath)):
            os.makedirs(os.path.dirname(newPath))
        shutil.move(inPath, newPath)
        print("=> compress " + filename)

        if copyJson:
            jsonPath = filename.replace(".png", ".json")
            if os.path.exists(jsonPath):
                newJsonPath = jsonPath.replace(root, outdir)
                shutil.copy(jsonPath, newJsonPath)
                print("=> copy json " + jsonPath)
            else:
                print("=> not json " + jsonPath)

    for filename in copyFile:
        inPath = filename
        newPath = filename.replace(root, outdir)
        if not os.path.exists(os.path.dirname(newPath)):
            os.makedirs(os.path.dirname(newPath))
        shutil.copy(inPath, newPath)
        print("=> copy " + filename)

        if copyJson:
            jsonPath = filename.replace(".png", ".json")
            if os.path.exists(jsonPath):
                newJsonPath = jsonPath.replace(root, outdir)
                shutil.copy(jsonPath, newJsonPath)
                print("=> copy json " + jsonPath)
            else:
                print("=> not json " + jsonPath)
    """

# 压缩文件，覆盖原始文件
def CompressOrigen(dir):
    pngFile = []
    print("=> check dir " + dir)
    for parent, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            if filename.find(".png") == -1:
                continue
            path = os.path.join(parent, filename)
            im = Image.open(path)
            if im.mode != "P":
                pngFile.append(path)
            im.close()

    for filename in pngFile:
        print("=> compress " + filename)
        # print(pngquant2Path + "\"" + filename + "\"")
        os.system(pngquant2Path + "\"" + filename + "\"")

