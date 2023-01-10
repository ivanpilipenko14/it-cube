a=int(input("введите место первой клетки"))
b=int(input("введите ряд первой клетки"))
c=int(input("введите место второй клетки"))
d=int(input("введите ряд второй клетки"))
f = (a-c)
g = (b-d)
n = (f % 1)
m = ( g %  1)
if n % 2 == 0 and m % 2 != 0 or n % 2 != 0 and m % 2 == 0 or n % 2 == 0 and m % 2 == 0 : 
    print("yes")
elif  n % 2 != 0 and m % 2 != 0 :
    print ("no")
