from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("http://127.0.0.1:5000/enter_invoice")

heading = driver.find_element(By.TAG_NAME, "h1").text
assert heading == "Enter Invoice", f"Unexpected heading: {heading}"
invoice_field = driver.find_element(By.ID, "invoice_number")
invoice_field.send_keys("INV12345")

save_button = driver.find_element(By.ID, "save_invoice")
save_button.click()


assert "showinvoice" in driver.current_url, "Did not navigate to showinvoice page"

print("Add Invoice test passed!")

driver.quit()
