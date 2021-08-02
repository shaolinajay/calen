#value declare
a=[]
n=int(input('enter the num'))
i=1
while i<=n:
    a.append(int(input("enter the values want to sort")))
    i+=1
print(a)
#intersection sort
for i in range(len(a)):
    temp=a[i]
    j=i-1
    while a[j]>temp and j>=0:
        a[j+1]=a[j]
        j=j-1
        a[j+1]=temp
print(a)
#bubble sort
for i in range(len(a)+4):
    for j in range(len(a)-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)
#mergesort
def mergesort(l):
    if len(l)>1:
        mid=len(l)//2
        left=l[:mid]
        right = l[mid:]
        mergesort(left)
        mergesort(right)


        i=0
        k=0
        j=0
        while len(left)>i and len(right)>j:
           if left[i]<right[j]:
             l[k]=left[i]
             i+=1
             k+=1
           else:
            l[k]=right[j]
            j+=1
            k+=1
        while len(left)>i:
           l[k]=left[i]
           k+=1
           i+=1
        while len(right)>j:
           l[k]=right[j]
           k+=1
           j+=1
t=(mergesort(a))
print(a)
#quick sort
def pvt(l,start,end):
    pivot=l[start]
    left=start+1
    right=end
    while (1):
        while left<=right and l[left]<=pivot:
            left+=1
        while right>=left and l[right]>=pivot:
            right=right-1
        if left<right:
            temp=l[left]
            l[left]=l[right]
            l[right]=temp
        else:
            break
    yet=l[start]
    l[start]=l[right]
    l[right]=yet
    return right
def quick_sort(l,start,end):
    if start<end:
     p=pvt(l,start,end)
     quick_sort(l,start,p-1)
     quick_sort(l,p+1,end)
quick_sort(a,0,len(a)-1)
print(a)
#selection sort
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)


