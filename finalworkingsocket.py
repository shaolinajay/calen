import socket
from time import sleep
from threading import Thread
import os
c=0
os.chdir("/storage/emulated/0/")
k="y"
alist=os.listdir()
for i in alist:
	if i=="socket":
		c=1
		break
if c==0:
	os.mkdir("socket")
def sender():
	def backward(c,find):
		if find!="/storage/emulated/0/":
			find=list(find)
			if find[-1]=="/":
				find.pop()
			copyfind=find.copy()
			for i in range(len(find)-1,-1,-1):
				if find[i]!="/":
					copyfind.pop(i)
				if find[i]=="/":
					copyfind.pop(i)
					break
			play=""
			for i in copyfind:
				play+=i
			return forward(c,play)
		else:
			print("ping=",find)
			return forward(c,find)		
	def forward(c,find):
		if find[-1]!="/":
			find+="/"
		os.chdir(find)
		print(addr)
		a=os.listdir()
		b=[".."]
		string=""
		for i in range(0,len(a)):
			b.append(a[i])
			if i==0:
				if os.path.isdir(a[i]):
					string+="$"+a[i]
				else:
					string+=a[i]
			else:
				if os.path.isdir(a[i]):
					string=string+"/$"+a[i]
				else:
					string=string+"/"+a[i]
		if len(string)==0:
			string+="$.."
		c.send(bytes(str(len(string)),"utf-8"))
		sleep(1)
		c.send(bytes(str(string),"utf-8"))
		sleep(1)
		file=c.recv(1024).decode()
		print("find=",find)
		if file in b:
			if file!="..":
				if os.path.isdir(file):
					finalfile=forward(c,find+file)
				else:
					if find[-1]=="/":
						return find+file
					else:
						return find+"/"+file
			elif file=="..":
				finalfile=backward(c,find)
			
			return finalfile
		else:
			finalfile=forward(c,find)
			return finalfile
	def pr(c,addr):
		file=forward(c,"/storage/emulated/0")
		p=open(file,"rb")
		p1=p.read()
		lp=len(p1)
		lp=bytes(str(lp),'utf-8')
		c.send(lp)
		sleep(1)
		print(file," downloading....")
		c.send(p1)
		sleep(2)
		print("download finished")
	s=socket.socket()
	s.bind(("192.168.43.1",9979))
	print("server started")
	s.listen(3)
	while True:
		c,addr=s.accept()
		if c:
			obj=Thread(target=pr,args=[c,addr])
			obj.start()
def receiver():
	def checktrue(c):
		count=0
		d=c.recv(1024).decode()
		d1=int(d)
		sleep(1)
		d2=int(d)
		print(d2)
		place=""
		while len(place)!=d1:
			if d2>1024:
				itval=c.recv(1024).decode()
				place+=itval
			else:
				itval=c.recv(d2).decode()
				place+=itval
			d2=abs(d2-1024)
		place=place.split("/")
		if "$.." in place:
			pass
		else:
			place.append("$..")
		place.sort()
		for i in range(0,len(place)):
			print(i,"=",place[i])
		dic={}
		dic1={}
		for i in range(0,len(place)):
			if place[i][0]=="$":
				dic1[str(i)]=place[i][1:]
			else:
				dic1[str(i)]=place[i]
		for i in place:
			if i[0]=="$":
				dic[i[1:]]="D"
			else:
				dic[i]="F"
		sleep(1)
		name=input("enter the file :")
		for k,v in dic1.items():
			if k==name:
				name=v
				break
		c.send(bytes(name,"utf-8"))
		if name in dic:
			if name!="..":
				for k,v in dic.items():
					if k==name:
						if v=="D":
							finalfile=checktrue(c)
						else:
							return name
			elif name=="..":
				finalfile=checktrue(c)
			return finalfile
		else:
			finalfile=checktrue(c)
			return finalfile
	c=socket.socket()
	c.connect(("192.168.43.1",9979))
	print("connected")
	finalfile=checktrue(c)
	c.send(bytes(finalfile,"utf-8"))
	pi=c.recv(1024)
	sleep(1)
	i=pi.decode("utf-8")
	v=int(i)
	rem=int(i)
	a=[]
	prefix="/storage/emulated/0/socket/"
	o=open(prefix+finalfile,"wb")
	p=b''
	while len(p)!=v:
		count=0
		if rem>1000000000:
			lt=c.recv(1000000000)
		else:
			lt=c.recv(rem)
		rem=abs(rem-1000000000)
		p+=lt
		value=str(round((len(p)/v)*100))
		for i in a:
			if value==i:
				count=1
		if count==0:
			print(value+"%")
			a.append(value)
	o.write(p)
a=input("  sender or receiver :")
if a[0]=="s":
	sender()
else:
	while k=="y":
		receiver()
		k=input("do you want to continue :")