'''
    跳转框架页：
        driver.switch_to
            frame()
            windows()
            alert()

'''


from selenium import webdriver


driver = webdriver.Chrome()

driver.get(r"F:/自动化测试18/练习的html/main.html")

driver.maximize_window()

# 跳转
driver.switch_to.frame("frame")

driver.find_element_by_xpath("//*[@id='input1']").send_keys("jason")




















