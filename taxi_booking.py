nat=1
class booked:
    def __init__(self,n,id,freetime,current,total):
        self.n=n
        self.id=id
        self.freetime=freetime
        self.current=current
        self.total=total
        self.dict={}
        self.pep=''
alist=[]
for i in range(1,5):
    obj=booked(1,i,6,"A",0)
    alist.append(obj)
def book():
    global nat
    pickup=input("pickup point :").upper()
    drop=input("drop point :").upper()
    picktime=int(input("pickup time :"))
    c=[]
    d=[]
    for i in alist:
        chrd=abs(ord(pickup)-ord(i.current))
        i.pep=chrd
    for i in alist:
        if i.freetime<=picktime:
            c.append(i)
    if len(c)==0:
        print("no taxi available to your required time")
    else:
        stfinals=sorted(c,key=lambda x:x.pep)
        lt=stfinals[0].pep
        for i in c:
            if i.pep==lt:
                d.append(i)
        stfinal=sorted(d,key=lambda x:x.total)
        verdictdist=abs(ord(pickup)-ord(drop))
        droptime=picktime+verdictdist
        distance=verdictdist*15
        amount=100+(distance-5)*10
        stfinal[0].dict[stfinal[0].n]={"id":stfinal[0].id,"customerid":nat,"bookingid":nat,"from":pickup,"to":drop,"pickuptime":picktime,"droptime":droptime,"amount":amount}
        stfinal[0].current=drop
        stfinal[0].total+=amount
        stfinal[0].freetime=droptime
        stfinal[0].n+=1
        nat+=1
def display():
    for i in alist:
        print("taxi-"+str(i.id),":",i.current,i.total)
        if len(i.dict)!=0:
         print(i.dict)
while(1):
    ch=int(input("1-Book or 2-display"))
    if ch==1:
        book()
    elif ch==2:
        display()

