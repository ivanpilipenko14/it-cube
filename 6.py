a=(input())
lst=[]
lst.extend(a)
if len(a)==7:
    print(a[0],",",a[1],a[2],a[3],",",a[4],a[5],a[6],sep="")
elif len(a)==3:
    print(a)
elif len(a)==5:
    print(a[0],a[1],",",a[2],a[3],a[4],sep="")
