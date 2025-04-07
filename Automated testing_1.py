from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


# 設置 ChromeOptions 模擬手機版瀏覽器 (這邊用 iPhone X)
mobile_emulation = {
    "deviceName": "iPhone X"
}

chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

# 設置 Chrome 驅動
driver = webdriver.Chrome(options=chrome_options)

# 打開官網
driver.get("https://www.cathaybk.com.tw/cathaybk/")

# 設置顯式等待
wait = WebDriverWait(driver, 10)

# 等待關鍵元素出現
wait = WebDriverWait(driver, 15)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.aem-container")))

# 獲取桌面路徑
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# 組合完整的路徑來保存截圖
screenshot_path = os.path.join(desktop_path, "screenshot.png")

# 截取頁面截圖並保存
driver.save_screenshot(screenshot_path)

# 關閉瀏覽器
driver.quit()
