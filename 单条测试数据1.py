'''
   1.准备数据
   2.调用被测方法，实现页面登陆逻辑
   3.获取实际结果与期望结果对比，断言
'''
from unittest import TestCase       # 单元测试
from selenium import webdriver      # selenium工具
import time                         # 时间
class TesHkr(TestCase):

    def TestLogin(self):       # 定义一个函数
        # 1准备数据
        username = "jason"
        pwd = "1234567"
        expect = "Student"     # 登陆成功依据
        # 2执行用例
        driver = webdriver.Chrome()      # 创建浏览器
        driver.get("http://localhost:8081/HKR")  # 获取网址
        driver.maximize_window()         # 屏幕最大化
        time.sleep(1)                    # 时间等待1秒
        driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)    # 输入账号
        driver.find_element_by_xpath("//*[@id='password']").send_keys(pwd)          # 输入密码
        driver.find_element_by_xpath("//*[@id='submit']").click()                   # 点击登陆
        # 3获取实际结果
        result = driver.title                    # 获取结果对象并返回值
        self.assertEqual(result, expect)         # 断言实际结果和期望结果是否一致

    def TestLoginError(self):  # 定义一个函数
        # 1准备数据
        username = "jason"
        pwd = "12345678"
        expect = "账户名错误或密码错误！别瞎弄"  # 登陆成功依据
        # 2执行用例
        driver = webdriver.Chrome()  # 创建浏览器
        driver.get("http://localhost:8081/HKR")  # 获取网址
        driver.maximize_window()  # 屏幕最大化
        time.sleep(1)  # 时间等待1秒
        driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)  # 输入账号
        driver.find_element_by_xpath("//*[@id='password']").send_keys(pwd)  # 输入密码
        driver.find_element_by_xpath("//*[@id='submit']").click()  # 点击登陆
        # 3获取实际结果
        result = driver.find_element_by_xpath("//*[@id='mag_uname']").text  # 定位元素并获取文本结果对象并返回值
        self.assertEqual(result, expect)  # 断言实际结果和期望结果是否一致



