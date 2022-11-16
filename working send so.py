import socket
import time
s=socket.socket()
s.bind(("192.168.43.1",9780))
s.listen(3)
f=open("/storage/emulated/0/socket/vi.txt","r")
client=f.read().split(" ")
a=[]
b=[]
st=""
f=open("/storage/emulated/0/socket/dj.mp4","rb")
sltf=open("/storage/emulated/0/socket/dj.mp4","rb")
le=len((sltf.read()))	
print(le)
le=le//4
le+=int(0.25*4)
print(le)
while True:
	p=f.read(le)
	if len(p)==0:
		break
	a.append(p)
for i in a:
	b.append(str(len(i)))
for i in range(0,len(b)):
	if i==0:
		st=st+b[i]
	else:
		st=st+"/"+b[i]
print(st)
c,ap=s.accept()
if ap[0] in client:
	pt=st.split("/")
	st=""
	for i in range((4-int(client[1])),len(a)):
		if i==(4-int(client[1])):
			st+=b[i]
		else:
			st=st+"/"+b[i]
	c.send(bytes(st,"utf-8"))
	time.sleep(1)
	for i in range(4-int(client[1])):
			a.pop(0)
	def send():
		global a
		with open("/storage/emulated/0/socket/vi.txt","w") as out:
				out.write(ap[0]+" "+str(len(a)))
		c.send(a[0])
		print("sended1")
		time.sleep(1)
		ok=c.recv(1024).decode()
		if ok=="ok":
			a.pop(0)
			if len(a)>=1:
				send()
			else:
				with open("/storage/emulated/0/socket/vi.txt","w") as out:
					pass
	send()
	print("89")
else:
	c.send(bytes(st,"utf-8"))
	time.sleep(1)
	def send():
		global a
		with open("/storage/emulated/0/socket/vi.txt","w") as out:
				out.write(ap[0]+" "+str(len(a)))
		c.send(a[0])
		print("sended1")
		time.sleep(1)
		ok=c.recv(1024).decode()
		if ok=="ok":
			a.pop(0)
			if len(a)>=1:
				send()
	send()
	print("89")
		
	