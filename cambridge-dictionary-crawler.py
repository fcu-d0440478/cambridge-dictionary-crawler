from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 設定 Edge 瀏覽器的選項
edge_options = Options()
# edge_options.add_argument("--headless")  # 啟用無頭模式
edge_options.add_argument("--window-size=1920x1080")  # 設定視窗大小
edge_options.add_experimental_option(
    "excludeSwitches", ["enable-logging"]
)  # 排除日誌開關

# 初始化 Edge WebDriver
driver = webdriver.Edge(options=edge_options)
driver.implicitly_wait(2)  # 隱性等待


def get_definition(driver, word):
    driver.get(f"https://dictionary.cambridge.org/zht/詞典/英語-漢語-繁體/{word}")
    xpath = "/html/body/div[2]/div/div[1]/div[2]/article/div[2]/div[4]/div/div/div/div[3]/div/div[2]/div[1]/div[3]/span"
    elements = driver.find_elements("xpath", xpath)
    for i in elements:
        print(f"{word}: {i.text}")


get_definition(driver, word="architect")
get_definition(driver, word="apple")
get_definition(driver, word="banana")
get_definition(driver, word="cat")
get_definition(driver, word="dog")
get_definition(driver, word="elephant")

# Close the WebDriver
driver.quit()
