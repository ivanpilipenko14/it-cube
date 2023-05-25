n=int(input("введите кол-во точек"))
h1=0
h2=0
h3=0
h4=0
for i in range(n):
    x=int(input())
    y=int(input())
    if x<0 and y>0:
        h2+=1
    elif x>0 and y>0:
        h1+=1
    elif x<0 and y<0:
        h3+=1
    elif x>0 and y<0:
        h4+=1
print("первая четверть",h1)
print("вторая четверть",h2)
print("третья четверть",h3)
print("четвертая четверть",h4)

        