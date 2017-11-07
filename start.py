# coding:utf8

outDir = "F:\\game\\release"
# projectDir = "E:\\lycq_trunk\\client\\project"
projectDir = "E:\\lycq\\client\\project"

# outDir = "F:\\ios_test"
# projectDir = "E:\\lycq_ios\\client\\project"

import gen_version.gen_start as gen_start
import gen_version.gen_version_code as gen_version_code
import os

input = raw_input("开始！！！(Yes/N)")
if input != "Yes":
    print("exit!!!")
    exit()
print("工程路径 => " + projectDir)
print("输出文件路径 => " + outDir)

curVersion = gen_version_code.GetMaxVersion(outDir)
print("当前版本号 => " + str(curVersion))

versionDir = os.path.join(outDir, str(curVersion))
if not os.path.exists(versionDir):
    print("not version dir!!!", versionDir)
    exit()

gen_start.Start(versionDir, projectDir, curVersion, outDir)