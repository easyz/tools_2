#coding:utf8

import os
import json
import hashlib
import sys
import math
import shutil

def GetMaxVersion(outDir):
    maxVersion = 0
    if os.path.exists(outDir):
        for dirName in os.listdir(outDir):
            try:
				if dirName.startswith("~"):
					dirName = dirName[1:]
				v = int(dirName)
				if v > maxVersion:
					maxVersion = v
            except:
                pass
    return maxVersion

def GetVersionList(outDir):
	def sortFun(lhs, rhs):
		return rhs - lhs

	array = []
	if os.path.exists(outDir):
		for dirName in os.listdir(outDir):
			try:
				if dirName.startswith("~"):
					dirName = dirName[1:]
				v = int(dirName)
				array.append(v)
			except:
				pass
	array.sort(sortFun)
	return array

# def GetMaxVersionPath(outDir):
#     version = GetMaxVersion(outDir) + 1
#     return os.path.join(outDir, str(version))

def GetFileMD5(filepath):
	if os.path.isfile(filepath):
		f = open(filepath,'rb')
		md5obj = hashlib.md5()
		md5obj.update(f.read())
		hash = md5obj.hexdigest()
		f.close()
		return str(hash).upper()
	return None

MAX_PATCH_NUM = sys.maxint
VERSION_FILE_NAME = "md5.json"
# CODE_FILE_NAME = "ver.json"
allMD5Dict = {}
md5FileCount = 0
MAP_DIR = "resource/assets/map"

def GetCodeFileName(v):
	return "ver"+str(v)+".json"

def GenMaxCodeFile(root):
	verList = []
	for filename in os.listdir(root):
		if filename.startswith("ver") and filename.endswith(".json"):
			code = -1
			try:
				code = int(filename.replace("ver", "").replace(".json", ""))
			except:
				pass
			if code != -1:
				verList.append(code)
	def sort(lhs, rhs):
		return rhs - lhs
	verList.sort(sort)
	return len(verList) > 0 and verList[0] or 0



def AddMd5File(outDir, path):
	configPath = path.replace(outDir + "\\", "").replace("\\", "/")
	md5 = GetFileMD5(path)
	allMD5Dict[configPath] = md5
	print(configPath, md5)

# 资源md5
def ParserResDir(dir):
	global md5FileCount
	# assetsDir = os.path.join(dir, "resource", "assets")
	# 生成所以文件md5
	assetsDir = dir
	for parent, dirnames, filenames in os.walk(assetsDir):
		for filename in filenames:
			path = os.path.join(parent, filename)
			configPath = path.replace(dir + "\\", "").replace("\\", "/")
			if configPath.find(MAP_DIR) != -1:
				continue
			md5 = GetFileMD5(path)
			if md5 == None:
				raise Exception(path, md5)
			md5FileCount = md5FileCount + 1
			allMD5Dict[configPath] = md5
			print(configPath, md5)
	if md5FileCount != len(allMD5Dict):
		raise Exception("len(allFiles) != len(allMD5Dict")
	print("file count => " + str(md5FileCount))

# 地图md5使用缩略图替代
def ParserMapDir(outVersionDir):
	mapPath = os.path.join(outVersionDir, MAP_DIR)
	if not os.path.exists(mapPath):
		print("[INFO] ParserMapDir not " + outVersionDir)
		return
	for dirName in os.listdir(mapPath):
		smllPath = os.path.join(mapPath, dirName, "small.jpg")
		configPath = smllPath.replace(outVersionDir + "\\", "").replace("\\", "/")
		md5 = GetFileMD5(smllPath)
		allMD5Dict[configPath] = md5
		print(configPath, md5)

def Gen(outVersionDir, v):
	ParserResDir(outVersionDir)
	ParserMapDir(outVersionDir)
	json.dump(allMD5Dict, file(os.path.join(outVersionDir, VERSION_FILE_NAME), "w"))
	# verFile = {}
	# for k in allMD5Dict:
	# 	verFile[k] = v
	# json.dump(verFile, file(os.path.join(outVersionDir, CODE_FILE_NAME), "w"))

def GenCodeConfig(outDir):
	allVersion = []
	def sort(lhs, rhs):
		return lhs - rhs
	for versionName in os.listdir(outDir):
		path = os.path.join(outDir, versionName, VERSION_FILE_NAME)
		if not os.path.exists(path):
			print("not file => " + path)
			continue
		v = -1
		try:
			v = int(versionName)
		except:
			pass
		if v != -1:
			allVersion.append(v)
	allVersion.sort(sort)
	allVersionConfig = []
	# print(allVersion)
	# 所以的配置文件
	for version in allVersion:
		path = os.path.join(outDir, str(version), VERSION_FILE_NAME)
		f = file(path, "r")
		allVersionConfig.append(json.load(f))
		f.close()

	if len(allVersion) == 0:
		print("all version empty!!!")
		return
	
	allVersion.reverse()
	allVersionConfig.reverse()

	curVersion = allVersion[0]
	curVersionConfig = allVersionConfig[0]
	cfg = {}
	for fileName in curVersionConfig:
		cfg[fileName] = curVersion
		for index in range(1, min(len(allVersion), MAX_PATCH_NUM)):
			v = allVersion[index]
			vmd5 = allVersionConfig[index][fileName]
			# 没有对应的资源
			if not vmd5:
				break
			# 如果是相同的资源，则更新版本号到旧的
			if vmd5 == curVersionConfig[fileName]:
				cfg[fileName] = v
			# 资源不同，中断查找
			else:
				break
	json.dump(cfg, file(os.path.join(outDir, "VERSION"), "w"))

	
def GenVersionCodeFile(root, version):
	# json.dump(allMD5Dict, file(os.path.join(outVersionDir, VERSION_FILE_NAME), "w"))
	print("MAX VERSION => " + str(version))
	path = os.path.join(root, str(version))
	if not os.path.exists(path):
		print("[ERROR] GenVersionCodeFile => " + path)
		return
	# maxMd5 = json.load(file(os.path.join(path, VERSION_FILE_NAME), "r"))
	# print(maxMd5)

	# array = GetVersionList(root)
	versionMd5 = []
	for v in GetVersionList(root):
		p = os.path.join(root, str(v), VERSION_FILE_NAME)
		print(p)
		if os.path.exists(p):
			versionMd5.append([v, json.load(file(p, "r"))])
		else:
			print("[ERROR] md5 file is null => " + p)

	# 新文件配置
	newDict = {}
	# 遍历所以版本
	for i in range(0, len(versionMd5)):
		lhsVersion = versionMd5[i][0]
		lhsMd5 = versionMd5[i][1]
		# 遍历到的版本文件
		for key in lhsMd5:
			codeV = lhsVersion
			# 如果新文件配置里面存在当前文件，并且版本号比遍历到文件号码较大，则不需要比较改文件
			# if newDict.get(key) != None and newDict.get(key) >= codeV:
			if newDict.get(key) != None:
				continue
			# if key == "resource/assets/atlas2_ui/cm/cm.png":
			# 	print("=============================1111" + str(codeV))
			# 向下查找最小的版本号
			tempmd5 = None
			for j in range(i, len(versionMd5)):
				v = versionMd5[j][0]
				md5 = versionMd5[j][1].get(key)
				if not md5:
					continue
				if md5 == lhsMd5[key]:
					codeV = v
				# if not md5 or lhsMd5[key] != md5:
				# 	break
				# else:
				# 	codeV = v
			# if key == "resource/assets/atlas2_ui/cm/cm.png":
			# 	print("=============================" + str(codeV))
			newDict[key] = codeV
	# for key in maxMd5:
	# 	codeV = version
	# 	for data in versionMd5:
	# 		v = data[0]
	# 		md5 = data[1].get(key)
	# 		if not md5 or maxMd5[key] != md5:
	# 			break
	# 		else:
	# 			codeV = v
	# 	newDict[key] = codeV

	simpleDict = {}
	for k in newDict:
		keyArray = k.split("/")
		tempDict = simpleDict
		length = len(keyArray)
		for i in range(0, length):
			value = keyArray[i]
			if tempDict.has_key(value):
				tempDict = tempDict[value]
			else:
				if i == length - 1:
					tempDict[value] = newDict[k]
				else:
					tempDict[value] = {}
					tempDict = tempDict[value]


	maxCode = GenMaxCodeFile(root) + 1
	print(maxCode)
	# json.dump(simpleDict, file("f:/test.json", "w"))
	json.dump(simpleDict, file(os.path.join(root, GetCodeFileName(maxCode)), "w"))
	# json.dump(newDict, file(os.path.join(root, GetCodeFileName(maxCode)), "w"))
	# print(newDict)	
	# for v in array:

def CheckDir(dir):
	if not os.path.exists(dir):
		os.makedirs(dir)
		
def UpNewVersionFile(root, version):
	newDir = os.path.join(root, "temp_upload")
	if os.path.exists(newDir):
		shutil.rmtree(newDir)
	
	codeFileName = GetCodeFileName(GenMaxCodeFile(root))
	p = os.path.join(root, codeFileName)
	if not os.path.exists(p):
		print("[ERROR] UpNewVersionFile Not Exists => " + p)
		return
	print(version, p)
	jsonDictObject = json.load(file(p, "r"))
	jsonObject = {}
	def readAllKey(prefix, dict):
		allDict = {}
		for key in dict:
			v = dict[key]
			if isinstance(v, int):
				# 根节点或者有版本的才需要写入配置
				# if prefix == "" or v != 1:
					allDict[prefix + key] = v
			else:
				temp = readAllKey(prefix + key + "/", v)
				for key in temp:
					allDict[key] = temp[key]
		return allDict

	

	jsonObject = readAllKey("", jsonDictObject)


	# print(jsonObject)
	# exit()
	for key in jsonObject:
		v = jsonObject[key]
		# print(v , version)
		if v == version:
			oldPath = os.path.join(root, str(version), key)
			newPath = os.path.join(root, "temp_upload", str(v), key)
			# print(oldPath + " ==> " +newPath)
			if key.startswith("resource/assets/map"):
				oldPath = oldPath.replace("/small.jpg", "").replace("\\", "/")
				newPath = newPath.replace("/small.jpg", "").replace("\\", "/")
				print("copy map =======> " + oldPath + "  =>  " + newPath)
				shutil.copytree(oldPath, newPath, False, None)
			else:
				print(oldPath + " ==> " +newPath)
				CheckDir(os.path.dirname(newPath))
				shutil.copy(oldPath, newPath)
	newPath = os.path.join(newDir, codeFileName)
	CheckDir(os.path.dirname(newPath))
	shutil.copy(p, newPath)
