from selenium import webdriver
import time
driver = webdriver.Chrome()   # 创建浏览器
driver.get("https://www.suning.com/")    # 打开苏宁网站
driver.maximize_window()      # 屏幕最大化
driver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys("iphone13")   # 输入买的东西
driver.find_element_by_xpath("//*[@id='searchSubmit']").click()                   # 点击搜索
driver.implicitly_wait(2)                                                         # 网页隐藏式时间等待2秒
time.sleep(3)                                                                     # 等3秒时间反应
driver.find_element_by_xpath('//*[@id="ssdsn_search_pro_baoguang-1-0-1_1_01:0000000000_12314319126"]/i/img').click()    # 选择手机
driver.implicitly_wait(2)                                                         # 网页隐藏式时间等待2秒
handle = driver.window_handles                                                    # 获取所有网页或手柄
driver.switch_to.window(handle[1])                                                # 获取第一页网页
driver.find_element_by_xpath('//*[@id="colorItemList"]/dd/ul/li[11]/a/span').click()     # 点击手机内存
driver.implicitly_wait(2)                                                         # 网页隐藏式时间等待2秒
handle = driver.window_handles                                                    # 获取所有网页或手柄
driver.switch_to.window(handle[1])                                                # 获取第一页网页
time.sleep(3)                                                                     # 等3秒反应
driver.find_element_by_xpath("//*[@id='addCart']").click()                        # 点击加入购物车  # 成功加入购物车
