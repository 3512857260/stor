from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
#  当前浏览器
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(1)

driver.get("https://www.jd.com/")
driver.implicitly_wait(2)
driver.find_element_by_xpath("//*[@id='ttbar-login']").click()
driver.find_element_by_xpath("//*[@class='login-tab login-tab-r']").click()
# 登录
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("17774062894")
driver.find_element_by_xpath("//*[@id='nloginpwd']").send_keys("123456")
driver.find_element_by_xpath("//*[@id='loginsubmit']").click()

driver.implicitly_wait(2)      # 隐藏式等2秒
ele = driver.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[3]')   # 滑动坐标点
Ac = ActionChains(driver)          # 把控制权交给Actionchains
Ac.click_and_hold(ele).move_by_offset(120,0).perform()     # 移动鼠标
Ac.release()  # 释放鼠标
driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/button').click()

driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div/div/div[1]/button').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/div[3]/button').click()
