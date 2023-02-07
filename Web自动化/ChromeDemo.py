from selenium import webdriver

# Chrome浏览器
driver = webdriver.Chrome()

'''
driver = webdriver.Firefox()    # Firefox浏览器
driver = webdriver.Chrome()     # Chrome浏览器
driver = webdriver.Ie()         # Ie浏览器
driver = webdriver.Edge()       # Edge浏览器
driver = webdriver.PhantomJS()  # PhantomJS()
'''

# 不自动关闭浏览器
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

# 将option作为参数添加到Edge中
driver = webdriver.Chrome(options=option)


driver.get('https://www.csdn.net/')

# 新标签中打开
# js = "window.open('https://blog.csdn.net/qq_43965708')"
# driver.execute_script(js)
