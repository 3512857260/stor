from selenium import webdriver

#  当前浏览器
driver = webdriver.Chrome()
driver.maximize_window()


driver.get("http://www.suning.com")
driver.implicitly_wait(2)  # 时间等待implicitly_wait(5)属于隐式等待，5秒钟内只要找到了元素就开始执行，5秒钟后未找到，就超时；
# time.sleep(5)表示必须等待5秒定位；
driver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys("联想拯救者y7000")
driver.find_element_by_xpath("//*[@id='searchSubmit']").click()

driver.implicitly_wait(2)  # 时间等待implicitly_wait(2)属于隐式等待，2秒钟内只要找到了元素就开始执行，2秒钟后未找到，就超时；
driver.find_element_by_xpath("//*[@id='0070094154-12233144535']/div/div/div[1]/div/a/img").click()

handle = driver.window_handles  # 1、页面切换2、在使用.click()切换页面后，获取最新的page_source
driver.switch_to.window(handle[1])   # 跳转到到第一个页面
# handles 中文：手柄，把手
driver.find_element_by_xpath("//*[@id='addCart']").click()
switch_to.window()
# 方法的使用：
# 1 handles = driver.window_handles          #获取当前浏览器的所有窗口句柄
# 2 driver.switch_to.window(handles[-1])     #切换到最新打开的窗口
# 3 driver.switch_to.window(handles[-2])     #切换到倒数第二个打开的窗口
# 4 driver.switch_to.window(handles[0])      #切换到最开始打开的窗口
