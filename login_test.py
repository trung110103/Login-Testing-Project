from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Khởi tạo ChromeDriver với Service
service = Service("C:\chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/login")

# Đăng nhập với thông tin hợp lệ
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CLASS_NAME, "radius").click()

# Kiểm tra đăng nhập thành công
success_message = driver.find_element(By.ID, "flash").text
assert "You logged into a secure area!" in success_message
print("Login successful!")

# Đợi 2 giây để xem kết quả
time.sleep(2)

# Đóng trình duyệt
driver.quit()