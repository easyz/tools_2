#coding:utf8
import os
import sys
import shutil

WORK = os.path.dirname(__file__)

sys.path.append(WORK + "/../")
import com.Log as Log
import com.Util as Util
import gen_version.compress_img as compress

OUT_ROOT = sys.argv[1]
IN_ROOT = sys.argv[2]

if not IN_ROOT:
    exit(0)

INPUT_TYPE = {}
INPUT_TYPE[1] = "body"
INPUT_TYPE[2] = "mon_show"
INPUT_TYPE[3] = "monster"
INPUT_TYPE[4] = "role_show"
INPUT_TYPE[5] = "skillEff"
INPUT_TYPE[6] = "uiEffe"
INPUT_TYPE[7] = "weapon"
INPUT_TYPE[8] = "wing"
INPUT_TYPE[9] = "hero"
INPUT_TYPE[10] = "hero_show"
INPUT_TYPE[11] = "pet"
INPUT_TYPE[12] = "sceneEff"
INPUT_TYPE[13] = "horse"

if __name__ == "__main__":

    input = raw_input("""需要要打包的类型：
    1、角色
    2、怪物展示
    3、怪物
    4、角色展示
    5、技能特效
    6、ui特效
    7、武器
    8、披风
    9、英雄
    10、英雄展示
    11、宠物
    12、场景
    13、坐骑
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
    outPath = os.path.join(OUT_ROOT, inputType)
    if os.path.exists(outPath):
        shutil.rmtree(outPath)
    shutil.copytree(inPath, outPath)
    compress.CompressOrigen(outPath)

    raw_input("finish！！！")
