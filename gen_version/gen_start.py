#coding:utf8

import gen_version_file as gen
import compress_img as com
import util as util
import gen_version_code as gen_code
import shutil
import os
import json

# outDir = "E:\\test_pack_atlas"
# projectDir = "E:\\lycq\\client\\project"


def Start(outDir, projectDir, version, root):
    print("gen_start!!!")
    # 版本路径

    STEP00 = "编译代码"
    STEP01 = "拷贝资源"
    STEP02 = "打包图集"
    STEP02_02 = "压缩图集"
    STEP03_01 = "压缩图片01"
    STEP03_02 = "压缩图片02"
    STEP04 = "生成版本MD5文件"
    STEP05 = "合并库文件"
    STEP06 = "生成版本号文件`"
    STEP07 = "新版本文件"

    step = [
        STEP00,

        # STEP01,

        # STEP02,
        # STEP02_02,

        # STEP03_01,
        # STEP03_02,

        # STEP05,

        STEP04,
        STEP06,
        STEP07,

    ]

    for s in step:
        print(s.decode("utf8").encode("gbk"))

    if raw_input("continue(y/n)") != "y":
        print("interrupt!!!")
        return

    def index(s):
        for v in step:
            if v == s:
                print(s.decode("utf8").encode("gbk"))
                return True
        return False

    if index(STEP00):
        print("===> STEP00")
        util.BuildScript(projectDir, outDir)

    if index(STEP01):
        print("===> STEP01")
        copyPath = [
            "resource\\cfg",

            # "resource\\assets\\image\\img",

            # "resource\\assets\\movie\\hero",

            # "resource\\sound",

            # "resource\\assets\\image\\other",

            # "resource\\assets\\atlas_ui",

            # "resource\\assets\\map",

            # "resource\\assets\\movie\\blood",
            # "resource\\image\\public",
        ]

        for path in copyPath:
            print("=> copy " + path)
            util.copyFiles(os.path.join(projectDir, path), os.path.join(outDir, path))

    # 2、打包图集
    if index(STEP02):
        print("===> STEP02")
        gen.PackAtals(projectDir, "resource\\assets\\atlas2_ui", outDir)
        gen.ResetAtalsConfig(projectDir, "resource", "assets/atlas2_ui", outDir)

    if index(STEP02_02):
        print("===> STEP02_02")
        gen.CompressAtals(os.path.join(outDir, "resource\\assets\\atlas2_ui"))

    # 3、压缩资源
    if index(STEP03_01):
        print("===> STEP03_01")
        compressPath = [
            "resource\\assets\\image\\item_single",
        ]
        for path in compressPath:
            com.Compress(projectDir, path, outDir)

    if index(STEP03_02):
        print("===> STEP03_02")
        compressPath2 = [
            "resource\\assets\\atlas_font",

            # "resource\\assets\\movie\\hero",
            # "resource\\assets\\movie\\body",
            # "resource\\assets\\movie\\monster",
            # "resource\\assets\\movie\\skillEff",
            # "resource\\assets\\movie\\uiEffe",
            # "resource\\assets\\movie\\weapon",
            # "resource\\assets\\movie\\wing",

            # "resource\\assets\\movie\\eff",
            # "resource\\assets\\movie\\warspirit",
            # "resource\\assets\\movie\\footstep",
        ]
        for path in compressPath2:
            com.Compress(projectDir, path, outDir, True)

    if index(STEP04):
        print("===> STEP04")
        gen_code.Gen(outDir, version)

    if index(STEP05):
        print("===> STEP05")
        util.MergerLib(outDir)

    if index(STEP06):
        print("===> STEP06")
        gen_code.GenVersionCodeFile(root, version)

    if index(STEP07):
        print("===> STEP07")
        gen_code.UpNewVersionFile(root, version)

    raw_input("\nfinish!!!")