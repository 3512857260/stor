from threading import Thread
import time
# money = 10000
s = 0
class cook(Thread):
    username = ""
    count = 0
    def run(self) -> None:
        global s
        while True:
            if s < 500:
                s = s + 1
                self.count = self.count + 1
                time.sleep(0.001)
            elif s == 500:
                time.sleep(3)
                if s == 500:
                    print(self.username, "造了", self.count, "个")
                    break
class program(Thread):
    username1 = ""
    count1 = 0
    def run(self) -> None:
        money = 10000
        global s
        while True:
            if money > 0:
                if s > 0 :
                    s = s - 1
                    money = money - 5
                    self.count1 = self.count1 + 1
                else:
                    time.sleep(0.01)
            else:
                print(self.username1, "抢了", self.count1, "您的余额为:", money, "元")
                break

c1 = cook()
c1.username = "刘备"
c2 = cook()
c2.username = "张飞"
c3 = cook()
c3.username = "关羽"
#
p1 = program()
p1.username1 = "宏一"
p2 = program()
p2.username1 = "蓝二"
p3 = program()
p3.username1 = "张三"
p4 = program()
p4.username1 = "李四"
p5 = program()
p5.username1 = "王五"
p6 = program()
p6.username1 = "赵六"


c1.start()
c2.start()
c3.start()
#
p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
p6.start()


