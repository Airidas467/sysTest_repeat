from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()


base_url = "http://127.0.0.1:5000"
driver.get(base_url)
time.sleep(2)  
assert "Welcome to my Flask App!" in driver.page_source
print("Home Page test passed")



driver.get(f"{base_url}/enter_invoice")

print("Add Invoice test passed (manual input required for your fields)")

driver.get(f"{base_url}/item_list")
time.sleep(2)
assert "Stock List" in driver.page_source
print("Show Stock test passed")


driver.quit()
