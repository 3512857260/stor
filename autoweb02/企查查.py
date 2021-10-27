from selenium import webdriver
import time
driver = webdriver.Chrome()  # 创建浏览器
driver.maximize_window()
driver.get("https://www.qcc.com/")                          # 打开企查查网页
driver.implicitly_wait(2)
time.sleep(5)
driver.find_element_by_xpath('/html/body/header/div/ul/li[10]/a/span').click()
driver.find_element_by_xpath("//*[@id='normalLogin']").click()
# 登录企查查
driver.find_element_by_xpath("//*[@id='nameNormal']").send_keys("17774062894")
driver.find_element_by_xpath("//*[@id='pwdNormal']").send_keys("123456")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="user_login_normal"]/button').click()