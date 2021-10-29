# html测试报告
from HTMLTestRunner import HTMLTestRunner       # 运行器
import unittest                                 # 单元测试
import os                                       # 系统
from threading import Thread                    # 多线程
class hespt(Thread):                            # pattern  文件名称  # description详细报告  # file 测试结果html报告
    pattern = ""                                # 必须使用pattern、description、file否则会出现错误
    description = ""
    file = ""
    def run(self) -> None:

        tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern=self.pattern)

        runner = HTMLTestRunner.HTMLTestRunner(
            title = "HKR系统测试报告",
            description= self.description,
            verbosity=1,
            stream=open(file=self.file,mode="w+",encoding="utf-8")
        )

        runner.run(tests)
hasp1 = hespt()
hasp1.pattern= "K1.py"
hasp1.description = "HKR系统成功登录测试"
hasp1.file = "HKR系统成功登录测试报告.html"
hasp1.start()
hasp2 = hespt()
hasp2.pattern = "K2.py"
hasp2.description = "HKR系统登录失败测试"
hasp2.file = "HKR系统登录失败测试报告.html"
hasp2.start()