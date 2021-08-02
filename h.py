class calen:
    pos1=1
    def __init__(self,date,month,year):
        self.date=date
        self.month=month
        self.year=year
    def calculate(self):
        ce=0
        for i in range(0,self.year,100):
          if i==0:
              pass
          elif i%400==0:
              ce=ce+6
          else:
              ce=ce+5
        z=ce%7
        globals()['pos1']=z


        oy=self.year-1
        find=oy%100
        leapf=find//4
        nolep=find-leapf
        totaly=leapf*2+nolep
        last=totaly%7


        m=0
        leapyear=(0,3,1,3,2,3,2,3,3,2,3,2,3)
        nonleapyear=(0,3,0,3,2,3,2,3,3,2,3,2,3)
        if self.year%400==0 or self.year%4==0 and self.year%100!=0:
            w=leapyear
        else:
            w=nonleapyear
        if self.month==1:
            pass
        else:
            for i in range(0,self.month):
                m=m+w[i]
        m1=m%7


        nmn=(last+z+m1+self.date)%7
        a=("sunday","monday","tuesday","wednesday","thursday","friday","saturday")
        return a[nmn]





