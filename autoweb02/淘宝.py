from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()     # 创建浏览器
driver.maximize_window()        # 屏幕最大化
driver.get("https://login.taobao.com/")    # 打开淘宝登录网页
driver.find_element_by_xpath("//*[@id='fm-login-id']").send_keys("17774062894")
driver.find_element_by_xpath("//*[@id='fm-login-password']").send_keys("123456")
driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
driver.implicitly_wait(2)   # 隐藏式等待2秒
ele = driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')  # 获取滑动原点
Ac = ActionChains(driver)      # 把控制权交给Actionchains
Ac.click_and_hold(ele).move_by_offset().perform(300,0)     # 移动鼠标

