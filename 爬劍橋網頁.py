import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


# 設定一些chrome瀏覽器的變數，做了headless(不會開瀏覽器)測試，請確認chrome版本有到60
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
# 抓取selenium webdriver位置
driver = webdriver.Edge()
driver.implicitly_wait(2)  # 隱性等待，使用一次整個程式過程皆有效
# wait = WebDriverWait(driver, 10)  #顯性等待用，不是所有清況都能用隱性等待解決

driver.get(
    "https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E-%E6%BC%A2%E8%AA%9E-%E7%B9%81%E9%AB%94/architect"
)
# xpath = "//span[@class='def-body']/span[@class='trans']"
xpath = "/html/body/div[2]/div/div[1]/div[2]/article/div[2]/div[4]/div/div/div/div[3]/div/div[2]/div[1]/div[3]/span"
elements = driver.find_elements("xpath", xpath)
for i in elements:
    print(i.text)
