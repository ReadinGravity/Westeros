a=int(input("strana a: "))
b=int(input("strana b: "))
c=int(input("strana c: "))

if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("rovnostranny trojuholnik")
    elif a==b or a==c or b==c:
        print("rovnoramenny trojuholnik")
    else:
        print("roznostranny trojuholnik")
    if a**2==b**2+c**2 or c**2==a**2+b**2 or b**2==a**2+c**2:
        print("pravouhly trojuholnik")
else:
    print("neexistujuci trojuholnik, tzv. mysticky")
