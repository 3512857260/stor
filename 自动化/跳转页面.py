from selenium import webdriver
import time
driver = webdriver.Chrome()     # 创建谷歌驱动
# 打开页面
driver.get(r"C:/Users/肖桂明/Desktop/python/自动化/自动化视频/自动化测试1/练习的html/跳转页面/pop.html")
driver.find_element_by_xpath("//*[@id='goo']").click()
# 跳转页面
driver.switch_to.alert.dismiss()