import random
# print("==============================================")
# print("|------------中国工商银行账户管理系统------------|")
# print("|------------1、开户              ------------|")
# print("|------------2、取钱              ------------|")
# print("|------------3、存钱              ------------|")
# print("|------------4、转账              ------------|")
# print("|------------5、查询              ------------|")
# print("|------------6、退出              ------------|")
# print("==============================================")
bank_name="汉科软地球中国区老牛湾分行"#全局变量
bank={}
# {'Frank': {'password': '123456', 'country': '中国', 'province': '沙河', 'street': '老牛湾', 'door': '0001', 'account': 60547549, 'bank_name': '汉科软地球中国区老牛湾分行', 'money': 0}}
#                # 元素1   ，元素 2 ，元素3
# def bank_useradd(username,password,country,province,street,door,account):
#     bank[username]={
#         "password":password,
#         "country":country,
#         "province":province,
#         "street":street,
#         "door":door,
#         "account":account,
#         "bank_name":bank_name,
#         "money":0
#     }
#     return 1
def useradd():
    username=input("请输入您的用户名")
    password=input("请输入您的密码")#print(bank[username]["password"])
    print("下面请您输入你的地址")
    country=input("\t\t请输入你所在的国家")
    province=input("\t\t请输入您的省份")
    street=input("\t\t请输入你的街道")
    door=input("\t\t请输入您的门牌号")
    account=random.randint(10000000,99999999)
    # money=0
    #             元素1    元素2
    status=bank_useradd(username,password,country,province,street,door,account)
    if status == 1:
        print("恭喜您成功开户，以下是您的个人信息：")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, bank[account]["money"], bank_name))
    if status == 2:
            print("用户账号已存在，请重新开户！")
    if status == 3:
            print("恭喜您成功开户，以下是您的个人信息：")
            info = '''
                                ------------个人信息------------
                                用户名:%s
                                账号：%s
                                密码：*****
                                国籍：%s
                                省份：%s
                                街道：%s
                                门牌号：%s
                                余额：%s
                                开户行名称：%s
                            '''
            # 每个元素都可传入%
            print(info % (username, account, country, province, street, door, bank[account]["money"], bank_name))
            print("用户库已注册满!")
#开户
def bank_useradd(username,password,country,province,street,door,account):
    if account in bank:
        return 2
    else:
        bank[account]={
            "用户名": username,
            "账号": account,
            "密码": password,
            "国籍": country,
            "省份": province,
            "街道": street,
            "门牌号": door,
            "money": 0,
            "开户行名称": bank_name
        }
        if len(bank)==100:
            return 3
        else:return 1
#存钱
def cq():
    i = 1
    while i==1:
        q =int(input("请输入您个账号"))
        if q in bank:
            w=int(input("请输入您的金额"))
            bank[q]["money"]=bank[q]["money"]+w
            print("存款成功")
            print("账户",bank[q]["账号"],"您的存款金额为:",bank[q]["money"])
            break
        else:i=False
        print("查询不到该账户")
def qq():
    a = 0
    while a==0:
        q=int(input("请输入您的账号"))
        if q in bank:
            m=input("请输入密码")
            if m in bank[q]["密码"]:
                print(m)
                e=int(input("请输入取款金额"))
                # print(bank[q]["money"])
                if e<=bank[q]["money"]:
                    bank[q]["money"] = bank[q]["money"] - e
                    print("转出成功")
                    return 0
                else:print("当前金额不存在")
                return 3
            else:print("您输入的密码不正确")
            return 2
        else:print("您输入的用户不存在")
        return 1
def zz():
    b = 0
    while b==0:
        z=int(input("请输入转出的账号"))
        if z in bank:
            x=int(input("请输入转入的账号"))
            if x in bank:
                c=input("请输入转出账号的密码")
                if c in bank[z]["密码"]:
                    print(c)
                    v=int(input("请输入转出金额"))
                    if v<=bank[z]["money"]:
                        bank[z]["money"]=bank[z]["money"]-v
                        bank[x]["money"]=bank[x]["money"]+v
                        print("转账成功")
                        print("您当前转出账号余额为:",bank[z]["money"])
                        print("您当前转入账号余额为:",bank[x]["money"])
                        return 0
                    else:print("您的余额不足")
                    return 3
                else:print("您输入的转出账号密码不正确")
                return 2
            else:print("您输入的转入账号不存在")
            return 1
        else:print("您输入的转出账号不存在")
        return 1
def cx():
    u = 1
    while u==1:
        i=int(input("请输入您的账号"))
        if i in bank:
            k=input("请输入您的密码")
            if k in bank[i]["密码"]:
                print(k)
                print("恭喜您成功开户，以下是您的个人信息：")
                print("用户名",bank[i]["用户名"])
                print("账号", bank[i])
                print("密码", bank[i]["密码"])
                print("国籍", bank[i]["国籍"])
                print("省份", bank[i]["省份"])
                print("街道", bank[i]["街道"])
                print("门牌号", bank[i]["门牌号"])
                print("money", bank[i]["money"])
                print("开户行名称", bank[i]["开户行名称"])
                print("恭喜您成功开户，以下是您的个人信息：")
                # info = '''
                #                                ------------个人信息------------
                #                                用户名:%s
                #                                账号：%s
                #                                密码：*****
                #                                国籍：%s
                #                                省份：%s
                #                                街道：%s
                #                                门牌号：%s
                #                                余额：%s
                #                                开户行名称：%s
                #                            '''
                # # 每个元素都可传入%
                # print(info % (username, account, country, province, street, door, bank[account]["money"], bank_name))
while True:
    print("==============================================")
    print("|------------中国工商银行账户管理系统------------|")
    print("|------------1、开户              ------------|")
    print("|------------2、取钱              ------------|")
    print("|------------3、存钱              ------------|")
    print("|------------4、转账              ------------|")
    print("|------------5、查询              ------------|")
    print("|------------6、退出              ------------|")
    print("==============================================")
    begin = input("请选择业务")
    if begin == "1":#开户
        useradd()
        # print(bank)
    elif begin == "2":#存钱
        cq()
    elif begin == "3":#取钱
        qq()
    elif begin == "4":#转账
        zz()
    elif begin == "5":#查询
        cx()
    elif begin == "6":#退出
        print("退出成功")
        break
    else:
        print("你瞎输入什么东西")
        break