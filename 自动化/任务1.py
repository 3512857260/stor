from selenium import webdriver
import time
driver = webdriver.Chrome()     # 创建谷歌驱动
# 打开页面
driver.get(r"C:/Users/肖桂明/Desktop/python/自动化/自动化视频/自动化测试1/练习的html/上传文件和下拉列表/autotest.html")
# 最大化maxinize
driver.maximize_window()
# 定位
time.sleep(5)
driver.find_element_by_id("accountID").send_keys("klos") # send.keys输入
driver.find_element_by_id("passwordID").send_keys("123456")
driver.find_element_by_id("areaID").send_keys("天津市")
driver.find_element_by_id("sexID1").click()  # click确定
driver.find_element_by_xpath("//*[@value='spring']").click()
driver.find_element_by_xpath("//*[@value='winter']").click()
# 系统框
driver.find_element_by_xpath("//*[@name='file' and @type='file']").send_keys(r"C:\Users\肖桂明\Pictures\Screenshots\mysql创建数据库和表.png")

driver.find_element_by_xpath("//*[@id='buttonID']").click()
driver.switch_to.alert.accept()