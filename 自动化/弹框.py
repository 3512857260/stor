from selenium import webdriver
import time
driver = webdriver.Chrome()     # 创建谷歌驱动
# 打开页面
driver.get(r"C:/Users/肖桂明/Desktop/python/自动化/自动化视频/自动化测试1/练习的html/弹框的验证/dialogs.html")
# 最大化
driver.maximize_window()
time.sleep(2)
# 定位元素
driver.find_element_by_xpath("//*[@id='alert']").click()
driver.switch_to.alert.accept()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='confirm']").click()
driver.switch_to.alert.dismiss()