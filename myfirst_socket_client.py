#server side program
import socket
from threading import Thread
from time import sleep
def pr(c,addr,lp):
	lp=bytes(str(lp),'utf-8')
	c.send(lp)
	sleep(1)
	print(lp)
	print(addr)
	c.send(p1)
s=socket.socket()
s.bind(("192.168.43.1",9999))
print("server started")
prefix="/storage/emulated/0/socket/"
file=input("enter the file you want to share :".upper())
p=open(prefix+file,"rb")
p1=p.read()
print(len(p1))
s.listen(3)
while True:
	c,addr=s.accept()
	if c:
		obj=Thread(target=pr,args=[c,addr,len(p1)])
		obj.start()
#client side program
import socket
import time
c=socket.socket()
c.connect(("192.168.43.1",9999))
pi=c.recv(1024)
time.sleep(1)
i=pi.decode("utf-8")
print("connected")
v=int(i)
rem=int(i)
a=[]
file=input("enter the file name :".upper())
prefix="/storage/emulated/0/socket/"
o=open(prefix+file,"wb")
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