#coding:utf8

"""
切除图片透明区域
"""

import sys
import os
import shutil
import json

# CONVERT_PATH = [
#     "E:\\lycq\\resource\\assets\\atlas2_ui\\image\\vip_show2"
# ]

WORK = os.path.dirname(__file__)

sys.path.append(WORK + "/../")
import com.Log as Log
import com.Util as Util
import gen_version.compress_img as compress

# for path in CONVERT_PATH:
#     if path == None or path == "":
#         Log.Info("没有配置解析路径")
#         exit()
#     if not os.path.exists(path):
#         Log.Info("不存在路径 " + path)
#         exit()

OUT_ROOT = "E:\\lycq\\resource\\assets\\image\\img\\"
IN_ROOT = "E:\\lycq\\resource\\assets_2\\image\\img\\"

exePath = os.path.join(WORK, "..\\gen_version\\libs\\texture_merger\\TextureMerger.exe")
if not os.path.exists(exePath):
    Log.Info("没有文件 TextureMerger")
    exit()

def Convert(inPath, outPath):
    Log.Info("提取目录 => " + inPath)
    if os.path.exists(outPath):
        shutil.rmtree(outPath)
    shutil.copytree(inPath, outPath)
    path = outPath
    packImgList = Util.GetAllFile(path, [".png"])
    for imgPath in packImgList:
        jsonPath = imgPath.replace(".png", ".json")
        command = "{0} -p {1} -o {2}".format(exePath, imgPath, jsonPath)
        os.system(command)
        print(imgPath)
    compress.CompressOrigen(outPath)

if __name__ == "__main__":

    input = raw_input("开始！！！(Yes/N)")
    if input != "Yes":
        print("exit!!!")
        exit()

    Log.Info("输出目录 => " + OUT_ROOT)

    Convert(os.path.join(IN_ROOT, "role_show"), os.path.join(OUT_ROOT, "role_show"))
    Convert(os.path.join(IN_ROOT, "vip_show"), os.path.join(OUT_ROOT, "vip_show"))
    Convert(os.path.join(IN_ROOT, "hero_show"), os.path.join(OUT_ROOT, "hero_show"))

    OUT_PUT_JSON_NAME = "slice_img.json"

    Log.Info("提取配置文件 ============> ")

    frames = {}
    for parent, dirnames, filenames in os.walk(OUT_ROOT):
        for filename in filenames:
            if filename == OUT_PUT_JSON_NAME:
                continue
            if filename.endswith(".json"):
                fullpath = os.path.join(parent, filename)
                fileObj = open(fullpath, "r")
                jsonObj = json.load(fileObj)
                for frame in jsonObj["frames"]:
                    frames[frame] = jsonObj["frames"][frame]
                fileObj.close()
                os.remove(fullpath)

    if len(frames) == 0:
        Log.Info(OUT_ROOT + " 没有json配置文件") 
    else:
        Log.Info("写入配置文件 => " + OUT_PUT_JSON_NAME)
        json.dump({"slice_img": frames}, open(os.path.join(OUT_ROOT, OUT_PUT_JSON_NAME), "w"))

    raw_input("finish！！！")
