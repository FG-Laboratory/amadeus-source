#!/usr/bin/env python3
import os,sys,time,json,urllib.request,subprocess

def ttt():
	return time.strftime("[%H:%M:%S]: ")

def bashExec(q):
	return subprocess.check_output(q,shell=True).decode("UTF-8")

import face_recognition
import numpy as np

def getFaceArray(fname):
	image = face_recognition.load_image_file(fname)
	return face_recognition.face_encodings(image)

def saveImage(url):
	bashExec("wget --tries=10 "+url+" -O tmpart.jpg 2>/dev/null")


tags=[]
faces=[]
meanfaces=[]

fls=os.listdir("face_recognitions/data")
for i in fls:
	if(i.count(".faces")==0):continue
	tags.append(i[:-6])
	fl=open("face_recognitions/data/"+i,"r")
	tmp=fl.readlines()
	fl.close()
	faces.append([])
	for f in tmp:
		faces[-1].append(np.array(json.loads(f)))
	meanfaces.append(sum(faces[-1])/len(faces[-1]))

def isItThisTag(ind,face):
	global faces
	tmpf=faces[ind]
	ress=[]
	for i in tmpf:
		ress.append( sum((face-i)**2) )
	return min(ress)**0.5

def findFaceByFile(fname):
	global tags,faces
	fcs=getFaceArray(fname)
	if(len(fcs)==0):return "none",[]
	res=[]
	for i in range(len(tags)):
		res.append(isItThisTag(i,fcs[0]))
	return tags[res.index(min(res))],res

def findFaceByUrl(url):
	saveImage(url)
	return findFaceByFile("tmpart.jpg")
