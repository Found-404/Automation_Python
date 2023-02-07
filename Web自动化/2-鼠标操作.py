# 简单的CSDN自动搜索脚本

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# 鼠标操作
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Edge()

# 不自动关闭浏览器
option = webdriver.EdgeOptions()
option.add_experimental_option("detach", True)

# 将option作为参数添加到Edge中
driver = webdriver.Edge(options=option)

driver.get('https://www.csdn.net/')
# 挂起
sleep(1)

# 定位搜索输入框
text_label = driver.find_element(by=By.ID, value="toolbar-search-input")

# 在搜索框中输入 python
text_label.send_keys('python')

# 右键搜索按钮
Searchbutton = driver.find_element(by=By.CSS_SELECTOR, value='#toolbar-search-button')
# 执行右键操作
ActionChains(driver).context_click(Searchbutton).perform()

# sleep(5)

# 鼠标悬停
wrapMore = driver.find_element(by=By.ID, value='floor-nav_557')
# 悬停
ActionChains(driver).move_to_element(wrapMore).perform()

# moreBd = driver.find_element(by=By.CSS_SELECTOR, value='.more-bd span:nth-child(6)')
# 执行单击操作
# moreBd.click()

sleep(2)
