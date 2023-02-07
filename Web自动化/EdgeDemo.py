from selenium import webdriver

# Edge浏览器
driver = webdriver.Edge()

'''
driver = webdriver.Firefox()    # Firefox浏览器
driver = webdriver.Chrome()     # Chrome浏览器
driver = webdriver.Ie()         # Ie浏览器
driver = webdriver.Edge()       # Edge浏览器
driver = webdriver.PhantomJS()  # PhantomJS()
'''

# 不自动关闭浏览器
option = webdriver.EdgeOptions()
option.add_experimental_option("detach", True)

# 将option作为参数添加到Edge中
driver = webdriver.Edge(options=option)


driver.get('https://www.csdn.net/')

# 新标签中打开
js = "window.open('https://blog.csdn.net/qq_43965708')"
driver.execute_script(js)

# 刷新页面
# driver.refresh()

# 获取打开的多个窗口句柄tab栏
# windows = driver.window_handles

# 切换到当前最新打开的窗口
# driver.switch_to.window(windows[-1])

