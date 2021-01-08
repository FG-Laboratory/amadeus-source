import os,sys,time,json,urllib.request,random,subprocess

def ttt():
	return time.strftime("[%H:%M:%S]: ")

#Получить JSON из адреса
def getJSON(url):
	time.sleep(0.34)
	bts = urllib.request.urlopen(url,timeout=40)
	s=bts.read().decode('UTF-8')
	bts.close()
	try:
		return json.loads(s)['response']
	except:
		print(ttt()+"Ошибка запроса! url="+url+";\n\t\tans="+s)
	return json.loads("{}")

def bashExec(q):
	return subprocess.check_output(q,shell=True).decode("UTF-8")

api_url="https://api.vk.com/method/"

vkToken=""#TODO

def getKagakuArts(tag):
	kurisuurls=[]
	tries=20
	while(len(kurisuurls)==0 and tries>0):
		try:
			j=getJSON("https://api.vk.com/method/wall.search?v=5.87&offset="+str(random.randint(0,20))+"&domain=steinsgate&query=%23"+tag+"&count=100&access_token="+vkToken)
			j=j['items']
			for i in j:
				if(i['text'].count("#")>3):continue
				try:
					for k in i['attachments']:
						try:kurisuurls.append(k['photo']['sizes'][-1]['url'])
						except:pass
				except:pass
		except Exception as e:print(e)
		tries-=1
	return kurisuurls

tagslist=['Rintarou', 'Mayuri', 'Itaru', 'Kurisu', 'Moeka', 'Ruka', 'Faris', 'Suzuha', 'Maho', 'Kagari', 'Takumi', 'Nanami', 'Rimi', 'Sena', 'Ayase', 'Yua', 'Kozue', 'Kaito', 'Akiho', 'Kona', 'Airi', 'Junna', 'Subaru', 'Toshiyuki', 'Takuru', 'Serika', 'Nono', 'Senri', 'Hana', 'Hinae', 'Uki', 'Mio', 'Yuuta', 'Ryouka', 'Miyuu', 'Sarai', 'Shun', 'Touko', 'Aria', 'Kiryuu', 'Ririka', 'Asuna']

import face_recognition

def getFaceArray(fname):
	image = face_recognition.load_image_file(fname)
	return face_recognition.face_encodings(image)

def saveImage(url):
	bashExec("wget --tries=10 "+url+" -O tmpart.jpg 2>/dev/null")

for tag in tagslist:
	arturls=[]
	try:
		arturls=getKagakuArts(tag)
	except Exception as e:
		print(e)
		continue
	for url in arturls:
		try:
			saveImage(url)
			faces=getFaceArray("tmpart.jpg")
			for f in faces:
				bashExec("echo \""+str(list(f))+"\" >> "+tag+".faces")
		except KeyboardInterrupt:
			break
		except Exception as e:
			print(e)
			time.sleep(1)
