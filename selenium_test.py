from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 创建一个Chrome浏览器实例
driver = webdriver.Chrome()

# 打开网页
driver.get("https://www.google.com")

# 找到搜索框元素并输入关键词
search_box = driver.find_element("name", "q")
search_box.send_keys("Python Selenium")

# 模拟键盘按下回车键
search_box.send_keys(Keys.RETURN)

# 等待一段时间，确保搜索结果加载完成
time.sleep(3)

# 获取搜索结果的标题和链接
results = driver.find_elements_by_xpath("//h3")  # 使用XPath选择标题元素
for result in results:
    title = result.text
    link = result.find_element_by_xpath("..").get_attribute("href")  # 获取父元素的链接
    print(f"Title: {title}")
    print(f"Link: {link}")
    print()

# 关闭浏览器
driver.quit()
