a=int(input("第一条边"))
b=int(input("第二条边"))
c=int(input("第三条边"))
if a+b>c and b+c>a and a+c>b:
    print("构成三角形")
    if a==b==c:
        print("")
    if a==b and a==c and b==c:
         print("等腰三角形")
    elif a*a+b*b==c*c:
        print("直角三角形")
    elif a+b>c:
         print("普通三角形")
else:
     print("不能形成三角形")