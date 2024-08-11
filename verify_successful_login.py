from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

# Setup Firefox WebDriver
service = Service('/usr/bin/geckodriver')  # Update path if necessary
options = Options()
options.headless = False  # Set to True for headless mode

driver = webdriver.Firefox(service=service, options=options)

# Open OpenMRS login page
driver.get("https://qa.kenyahmis.org/openmrs/spa/login")
# Or use the alternative URL
# driver.get("https://kenyaemr.nascop.org/openmrs/spa/login")

# Maximize the browser window
driver.maximize_window()

# Perform login
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

username_field.send_keys("admin")
password_field.send_keys("Admin123")

time.sleep(1)

login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Verification
time.sleep(3)

try:
    # Check if a dashboard element exists (e.g., a link to the home page)
    dashboard_element = driver.find_element(By.XPATH, "//a[@href='/openmrs/spa/home']")
    print("Login successful.")
except:
    print("Login failed.")

# Alternatively, check for a specific URL
current_url = driver.current_url
if "home" in current_url:
    print("Login successful, redirected to home page.")
else:
    print("Login failed, not redirected to home page.")

# Close the browser
driver.quit()

