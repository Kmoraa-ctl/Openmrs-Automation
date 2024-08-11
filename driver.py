from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the Firefox driver
driver = webdriver.Firefox()

try:
    error_message = driver.find_element(By.XPATH, "//span[contains(text(), 'Invalid username or password. Please try again.')]")
    print("Error message found:", error_message.text)
except:
    print("No error message found")

try:
    driver.find_element(By.XPATH, "//span[contains(text(), 'Home')]")
    print("Home element found")
except:
    print("Home element not found")

