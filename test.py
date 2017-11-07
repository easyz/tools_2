
import os
import PIL.Image as Image

# array = []
# for i in range(1, 10):
#     array.append(10 - i)
# array.sort(lambda(lhs, rhs): return lhs-rhs)
# print(array)

allSize = 0

def PrintImgSize(imgPath):
    if not os.path.exists(imgPath):
        print("not found => " + imgPath)
        return
    global allSize
    imgData = Image.open(imgPath)
    # print(imgData.size)
    print(imgPath, imgData.size[0], imgData.size[1])
    allSize = allSize + imgData.size[0] * imgData.size[1]
    imgData.close()

def Load(resName, sex, direction, action):
    respath = "E:\\lycq\\resource\\assets\\movie\\body\\" + ("body" + resName + "_" + sex + "_" + direction + action) + ".png"
    PrintImgSize(respath)

def Load2(resName):
    for sex in range(0, 2):
        for dir in range(0, 5):
            Load(resName, str(sex), str(dir), "a")
            Load(resName, str(sex), str(dir), "c")
            Load(resName, str(sex), str(dir), "r")
            Load(resName, str(sex), str(dir), "s") 

# Load2("000")
# Load2("001")
# Load2("002")
# for i in range(1, 13):
#     Load2(str(100 + i))

# for i in range(1, 13):
#     Load2(str(200 + i))

# for i in range(1, 13):
#     Load2(str(300 + i))


# def LoadHero(type, resName, direction, action):
#     respath = "E:\\lycq\\resource\\assets\\movie\\" + type + "\\" + (type + resName + "_" + direction + action) + ".png"
#     PrintImgSize(respath)

# def LoadHero2(type, resName):
#         for dir in range(0, 5):
#             LoadHero(type, resName, str(dir), "a")
#             LoadHero(type, resName, str(dir), "c")
#             LoadHero(type, resName, str(dir), "r")
#             LoadHero(type, resName, str(dir), "s") 

# for i in range(1, 10):
#     LoadHero2("hero", str(1000 + i))            

# for i in range(1, 10):
#     LoadHero2("monster", str(10000 + i))      

def GetAllImgPath(fileDir):
    imgList = []
    # for fileName in os.listdir(fileDir):
    for fileDir, sub, fileList in os.walk(fileDir):
        for fileName in fileList:
            if fileName.endswith("png") or fileName.endswith(".jpg"):
                imgList.append(os.path.join(fileDir, fileName))
        
    # print(os.walk(fileDir))
        # if fileName.endswith("png"):
        #     imgList.append(os.path.join(fileDir, fileName))
    return imgList

def PrintSize(dir):
    for path in GetAllImgPath(dir):
        PrintImgSize(path)

PrintSize("E:\\lycq\\resource\\assets\\movie\\body")
# PrintSize("E:\\lycq\\resource\\assets\\movie\\weapon")
# PrintSize("E:\\lycq\\resource\\assets\\movie\\wing")
# PrintSize("E:\\lycq\\resource\\temp_out_movie\\wing")
# PrintSize("F:\\game\\release\\~213\\resource\\assets\\atlas2_ui")
# PrintSize("E:\\lycq\\resource\\temp_out_movie\\body")

print(allSize * 1)

# 29 541 516