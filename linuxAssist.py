#!/usr/bin/env python3
import utils,os,fractions
import numpy as np
from sympy import Matrix

links="/usr/share/applications/"
localLinks="/home/konstantin/.local/share/applications/"
commands=[]
keywords=[]


'''print("Загрузка ярлыков Ассистента...")
files1=os.listdir(links)
for i in files1:
	if(i[-min(len(i),len(".desktop")):]!=".desktop"):continue
	try:
		cmd="gtk-launch "+i[:-len(".desktop")]#utils.bashExec("cat "+links+i+" | grep ^Exec=")[5:-1]
		commands.append(cmd)
		kws=utils.bashExec("cat "+links+i+" | grep ^Name=")[5:-1]
		keywords.append(kws)
	except Exception as e:
		print(e)

files2=os.listdir(localLinks)
for i in files2:
	if(i[-min(len(i),len(".desktop")):]!=".desktop"):continue
	try:
		cmd="gtk-launch "+i[:-len(".desktop")]#utils.bashExec("cat "+localLinks+i+" | grep ^Exec=")[5:-1]
		commands.append(cmd)
		kws=utils.bashExec("cat "+localLinks+i+" | grep ^Name=")[5:-1]
		keywords.append(kws)
	except Exception as e:
		print(e)

print("Загрузка ярлыков Ассистента завершена")'''

class getAnswer():
	def __init__(self):
		pass
	def __repr__(self):
		return "<Linux Assistant>"
	def getAnswerByDial(self,arr):#Для совместимости с адаптерами
		cmd=arr[-1].lower()
		if(cmd.count("/pause")>0):
			cmd=cmd.split("/pause")[-1].replace("/pause","")
#		print("Assist:",cmd)
		score=0
		warr=utils.str2arr(cmd)
		if(warr[0] in ["курису","амадей","amadeus","амадеус","ассистент","кристина"]):warr.pop(0)
		if(warr[0].count("включи")+warr[1].count("музык")>1):
			try:
				pth=os.path.expanduser("~/Музыка")+"/"#TODO: English
				fls=os.listdir(pth)
				priors=[]
				for i in fls:
					tmpi=i.lower()
					if(tmpi.count("stein")+tmpi.count("takeshi")+tmpi.count("s;g")+tmpi.count("штейн")>0):priors.append(i)#Штайнера и Штайна игнорим. Не канон.
				cmd="vlc --open"# --random"
				for i in priors:#Сначала воспроизводим относящееся к тематике Калитки
					cmd+=" \""+pth+i+"\""
				for i in fls:
					cmd+=" \""+pth+i+"\""
				os.system(cmd+" 2>&1 &")
				return 0.9,"Выполнено!"
			except Exception as e:print(e)
		if("определител" in cmd and "матриц" in cmd):
			try:
				m=utils.bashExec("xclip -o")
				m=m.replace("{","[").replace("}","]").replace("\n","")
				D=np.linalg.det(eval(m))
				return 0.9,"Определитель равен "+str(fractions.Fraction(D))
			except Exception as e:
				print(e)
				return 0.7,"Произошла ошибка "+utils.entoru(str(e))
		if("собствен" in cmd and "значения" in cmd and "матриц" in cmd):
			try:
				m=utils.bashExec("xclip -o")
				m=m.replace("{","[").replace("}","]").replace("\n","")
				eigvals=np.linalg.eig(eval(m))[0]
				print(eigvals)
				res=""
				for i in range(len(eigvals)):res+=str(fractions.Fraction(eigvals[i]))+", "
				return 0.9,"Собственные значения "+res[:-2]
			except Exception as e:
				print(e)
				return 0.7,"Произошла ошибка "+utils.entoru(str(e))
		if("собствен" in cmd and "вектор" in cmd and "матриц" in cmd):
			try:
				m=utils.bashExec("xclip -o")
				m=m.replace("{","[").replace("}","]").replace("\n","")
				m=Matrix(eval(m))
				vects=m.eigenvects()
				res=""
				for v in vects:
					val=str(v[0])
					vv=str(v[2]).replace("[","").replace("]","").replace("\n","")[6:]
					res+="/pause Значение "+val+" - "+vv
				'''eigvals,eigvect=np.linalg.eig(eval(m))
				print(eigvals,eigvect)
				res=""
				zeros=[0 for x in range(len(eigvals))]
				for i in range(len(eigvals)):
					res+="Значение "+str(fractions.Fraction(eigvals[i]))+" - ["
					curvect=zeros.copy()
					curvect[i]=1
					curvect=eigvect.dot(curvect)
					curvect/=min(curvect)
					for j in range(len(curvect)):res+=str(fractions.Fraction(curvect[j]))+", "
					res=res[:-2]+'],'''
				return 0.9,"Собственные вектора "+res
			except Exception as e:
				print(e)
				return 0.7,"Произошла ошибка "+utils.entoru(str(e))
		return 0,""

