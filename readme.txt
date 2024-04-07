# README

## 劍橋詞典爬蟲工具

這個 Python 腳本使用 Selenium 自動化庫來抓取劍橋詞典網站上指定單詞的中文解釋。

### 功能

- 爬取劍橋詞典網站上的單詞解釋。
- 將抓取到的中文解釋輸出到控制台。

### 如何使用

1. 確保您的系統已安裝 Python 和 Selenium。
2. 將此腳本保存到本地文件。
3. 在終端或命令提示符中運行腳本。

### 腳本設定

- `edge_options`：設定 Edge 瀏覽器的選項，包括無頭模式和視窗大小。
- `webdriver.Edge`：初始化 Edge WebDriver。
- `driver.implicitly_wait`：設定隱性等待時間。
- `get_definition` 函數：接受 WebDriver 和單詞作為參數，訪問劍橋詞典網站並抓取單詞的中文解釋。

### 注意事項

- 如果您啟用無頭模式，請取消註釋 `edge_options.add_argument("--headless")` 這行代碼。