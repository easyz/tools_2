import os
import json
import shutil

# def GetAllImg(fileDir, prefix):
#     imgList = []
#     for fileDir, sub, fileList in os.walk(fileDir):
#         for fileName in fileList:
#             if fileName.endswith("png"):
#                 imgList.append(os.path.join(prefix, fileName))
#     return imgList

# allFile = GetAllImg("E:\\lycq\\client\\project\\resource\\assets\\movie\\body", "resource/assets/movie/body/")
# fd = file("E:/test.txt", "w")
# fd.write(str(allFile))
# fd.close()
# print(allFile)

def Copy(filePath, prefix):
    if not os.path.exists(filePath):
        print("[ERR] -------------------------------------" + filePath)
        return
    # shutil.copyfile(filePath, "f:/test/" + prefix)
    fDir = "f:/test/" + prefix
    if not os.path.exists(fDir):
        os.makedirs(fDir)
    print(filePath)
    shutil.copy2(filePath, fDir)

def CopyFile(prefix, jsonObj):
    for k in jsonObj:
        value = jsonObj[k]
        fName = prefix + k
        if type(value) == int:
            # print(fName, value)
            fPath = "F:/game/release/" + str(value) + "/" + fName
            # print(fPath)
            Copy(fPath, prefix)
            # return
        else:
            CopyFile(fName + "/", value)

jsonObj = json.load(file("F:\\game\\release\\ver285.json"))
CopyFile("", jsonObj)
# print(jsonObj)