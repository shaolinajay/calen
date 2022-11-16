import socket
from time import sleep
c = socket.socket()
c.connect(("192.168.43.1", 9780))
p = b''
l = c.recv(1024).decode()
sir = l.split("/")
print("value",l)
sleep(1)
def receive(k):
    global p
    o = b''
    l1 = int(k)
    rem = int(k)
    print(l1)
    while len(o) != l1:

        if rem > 10000000000:
            u = c.recv(10000000000)
        else:
            u = c.recv(rem)
        rem = abs(rem - 10000000000)
        o += u
        print((len(o) / l1) * 100)
        print(len(o)==l1)
    p += o
    y.write(o)
    print("rihted",len(p))
    sleep(1)
    c.send(bytes("ok","utf-8"))
ut=b''
try:
    read=open("/storage/emulated/0/video.mp4", "rb")
    ut=read.read()

except:
    print("nope")
y=open("/storage/emulated/0/video.mp4", "wb")
y.write(ut)
for i in range(0, len(sir)):
    receive(sir[i])