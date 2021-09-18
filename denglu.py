a=0
# b=str(input(root))
# c=str(input(admin))
while a<3:
    e= str(input("用户名"))
    f= str(input("密码"))
    if  e=="root" and f=="admin":
        print("登录成功")
        break
    else:
        print("登录错误,请重新输入")
        a=a+1