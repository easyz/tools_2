#coding:utf8
import os
import sys
import shutil

OUT_ROOT = "F:\\test2"
IN_ROOT = "E:\\lycq\\client\\project\\resource\\assets\\map"
FILE_NAME = "small.jpg"

for dirName in os.listdir(IN_ROOT):
    path = os.path.join(IN_ROOT, dirName, FILE_NAME)
    shutil.copy2(path, os.path.join(OUT_ROOT, dirName + ".jpg"))
    # print(filePath)
