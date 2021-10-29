from unittest import TestCase                           # 导入单元测试
from ddt import ddt                                     # 导入ddt模块
from ddt import data                                    # 导入ddt中的data数据包
from ddt import unpack                                  # 导入ddt中的unpack断言
import time                                             # 时间等待
from InitPage import InitPage                           # 导入自定义数据包
from LoginOperation import LoginOperation               # 导入自定义逻辑操作
from selenium import webdriver                          # 导入执行页面操作器
@ddt
class stdang(TestCase):
    @data(*InitPage.login_error_data)
    def testLoginError(self, testdata):
        username = testdata["username"]
        pwd = testdata["pwd"]
        expect = testdata["expect"]

        # 执行登陆
        driver = webdriver.Chrome()
        loginop = LoginOperation(driver)

        loginop.login(username, pwd)

        #  获取实际结果
        result = loginop.getError_result()

        driver.quit()

        self.assertEqual(result, expect)