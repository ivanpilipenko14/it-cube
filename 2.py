s=input("введите натуральные числа")
counter=0
lst=[]
lst.extend(s)
print(lst)
long=len(lst)
for i in range(long): 
    if i<i+1:
        counter+=1
print(counter-1)
