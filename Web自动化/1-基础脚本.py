from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get('https://www.csdn.net/')

# sleep([number])推迟调用线程的运行，可通过参数secs指秒数，表示进程挂起的时间。
sleep(2)

# 定位搜索输入框 (类似于ID选择器)
text_label = driver.find_element(by=By.ID, value="toolbar-search-input")

# 在搜索框中输入 FOund404
text_label.send_keys('FOund404')

sleep(2)
# 清除搜索框中的内容
text_label.clear()

# 输出搜索框元素是否可见
print(text_label.is_displayed())
# 输出placeholder的值
print(text_label.get_attribute('placeholder'))

# 定位搜索按钮 (类似于后代选择器)
button = driver.find_element(by=By.CSS_SELECTOR, value='#toolbar-search-button span')
# 输出按钮的大小
print(button.size)
# 输出按钮上的文本
print(button.text)

'''输出内容
True
python面试100问
{'height': 32, 'width': 28}
搜索
'''
