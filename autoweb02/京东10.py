from selenium import webdriver
import time
driver = webdriver.Chrome()    # 创建浏览器
driver.get("https://www.jd.com/")    # 打开京东网站
driver.maximize_window()            # 屏幕最大化
driver.find_element_by_id("key").send_keys("苹果13")
driver.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
driver.implicitly_wait(2)
# 选择要买的东西
driver.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[1]/a/img').click()
driver.implicitly_wait(2)
time.sleep(3)
handle = driver.window_handles
driver.switch_to.window(handle[1])
driver.find_element_by_xpath('//*[@id="InitCartUrl"]').click()    # 成功购物
