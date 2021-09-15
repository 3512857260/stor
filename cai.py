import random #import 引入模块、包。
ran=random.randint(0,80)
a=500
b=0
while True:
    print(ran)
    num=int(input("请输入一个数字"))

    if num == ran:
        print("OK")
        a=a+10
        print(a)
    elif b==2:
        break
    else:
        print("no")
        a=a-100
        print(a)
        i=i+1
