import random
ran= random.randint(1,80)
print(ran)
set=500#set(元组)跳出本次循环continue
while True:
    sum= int(input("请输入一个数字"))
    if ran==sum:
        print("恭喜你猜对了")
        set=set+100
        print(set)
    elif set<=0:
        break
    else:
        print("请重新猜")
        set=set-100
        print(set)

