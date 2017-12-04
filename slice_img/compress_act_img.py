#coding:utf8
import os
import sys
import shutil

WORK = os.path.dirname(__file__)

sys.path.append(WORK + "/../")
import com.Log as Log
import com.Util as Util
import gen_version.compress_img as compress

OUT_ROOT = "E:\\lycq\\resource\\assets\\movie\\"
IN_ROOT = "E:\\lycq\\resource\\assets_2\\movie\\"

INPUT_TYPE = {}
INPUT_TYPE[1] = "wing"
INPUT_TYPE[2] = "body"
INPUT_TYPE[3] = "weapon"
INPUT_TYPE[4] = "monster"
INPUT_TYPE[5] = "hero"
INPUT_TYPE[6] = "skillEff"
INPUT_TYPE[7] = "uiEffe"
INPUT_TYPE[8] = "pet"

if __name__ == "__main__":

    input = raw_input("""需要要打包的类型：
    5、英雄
    6、技能
    7、ui特效
    8、宠物
    """.decode("utf8").encode("gbk"))
    input = int(input or 0)

    if not INPUT_TYPE.has_key(input):
        print("exit!!!")
        exit()

    inputType = INPUT_TYPE[input]
    Log.Info("输出目录类型 => " + inputType)

    inPath = IN_ROOT + inputType
    if not os.path.exists(inPath):
        print("not " + inPath)
        exit()
    outPath = OUT_ROOT + "\\" + inputType
    if os.path.exists(outPath):
        shutil.rmtree(outPath)
    shutil.copytree(inPath, outPath)
    compress.CompressOrigen(outPath)

    raw_input("finish！！！")
