# 简单的键盘操作

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# 键盘操作
from selenium.webdriver.common.keys import Keys


driver = webdriver.Edge()
# 不自动关闭浏览器
option = webdriver.EdgeOptions()
option.add_experimental_option("detach", True)
# 将option作为参数添加到Edge中
driver = webdriver.Edge(options=option)
driver.get('https://www.csdn.net/')
# 挂起
sleep(1)

# input搜索框
inputSearch = driver.find_element(by=By.ID, value="toolbar-search-input")

# 定位输入框并输入文本
inputSearch.send_keys('测试输入文本')



# 使用 Backspace 来删除一个字符
inputSearch.send_keys(Keys.BACK_SPACE)

sleep(0.5)

# Ctrl + A 全选输入框中内容
inputSearch.send_keys(Keys.CONTROL, 'a')
sleep(0.5)

# Ctrl + C 复制输入框中内容
inputSearch.send_keys(Keys.CONTROL, 'c')
sleep(0.5)
inputSearch.send_keys(Keys.BACK_SPACE)  # 删除所有字符
sleep(0.5)
# Ctrl + V 粘贴输入框中内容
inputSearch.send_keys(Keys.CONTROL, 'v')

# 模拟回车键进行跳转（输入内容后）
inputSearch.send_keys(Keys.ENTER)
