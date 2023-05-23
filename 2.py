m=int(input("масса"))
h=m=int(input("рост"))
i= m/h**2
if 18.5<i<25:
    print("оптимальная масса ")
elif i>25:
    print("избыточная масса ")
elif 18.5>i:
    print("недостаточная масса")

