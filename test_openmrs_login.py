from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (Firefox)
driver = webdriver.Firefox()

# Navigate to the OpenMRS login page
driver.get("https://qa.kenyahmis.org/openmrs/spa/login")

# Find the username and password fields and enter the credentials
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

username_field.send_keys("admin")
password_field.send_keys("Admin123")

# Click the login button
login_button = driver.find_element(By.ID, "loginButton")
login_button.click()

# Wait for the page to load
time.sleep(5)

# Verify successful login by checking the presence of an element unique to the landing page
try:
    driver.find_element(By.XPATH, "//span[contains(text(), 'Home')]")
    print("Login successful!")
except:
    print("Login failed!")

# Close the browser
driver.quit()

