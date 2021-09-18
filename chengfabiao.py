#外层循环i 纵向坐标
i=1
while i<=9:
#内层循环a开始 横向坐标
    a=1
    while a<i+1:
        print(str(i)+"x"+str(a)+"="+str(i*a)+"  ",end="")
        a=a+1
#内循环结束a
    i=i+1
    print()
#横向或纵向自己设置即可




