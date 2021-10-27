from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()     # 创建浏览器
driver.maximize_window()        # 屏幕最大化
driver.get("https://passport.suning.com//")    # 打开苏宁登录网页
driver.implicitly_wait(2)
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/a[2]').click()
# 登录苏宁
driver.find_element_by_xpath('//*[@id="showErrorUsernameDiv"]/label').send_keys("17774062894")
driver.find_element_by_xpath('//*[@id="showErrorPwdDiv"]/label').send_keys("123456")
# ele = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[2]/div[2]/div/div[3]"]')  # 获取滑动原点
# Ac = ActionChains(driver) # 把控制权交给Actionchains
# try:
#     for i in range(100,200):
#         Ac.click_and_hold(ele).move_by_offset().perform(i)   # 移动鼠标
#         Ac.release()
# except Exception:
#     print("验证通过")
# finally:
#     driver.find_element_by_xpath('//*[@id="submit"]').click()