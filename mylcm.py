a=[]
n=int(input("enter numbers to want"))
for i in range(n):
	a.append(int(input("enter the numbers")))
a.sort()
high=a[-1]
turn=1
def call():
	global turn,high
	for x in range(len(a)):
		if high%a[x]==0:
			if a[x]==a[len(a)-1]:
				turn=0
		else:
			high+=1
			break
	return True
while True:
	if call():
		if turn==0:
			print(high)
			break
	
	