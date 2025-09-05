from selenium import webdriver
from selenium.webdriver.common.by import By

# Open Firefox
driver = webdriver.Firefox()

# Navigate to your Flask app
driver.get("http://127.0.0.1:5000/")

# Verify the heading text
heading = driver.find_element(By.TAG_NAME, "h1").text
assert heading == "Welcome to my Flask App!", f"Unexpected heading: {heading}"

print("Home page test passed!")

# Close the browser
driver.quit()
