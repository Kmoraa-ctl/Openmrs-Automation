import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import HtmlTestRunner

class OpenMRSTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://qa.kenyahmis.org/openmrs/spa/login")
        self.wait = WebDriverWait(self.driver, 10)
    
    def test_login_success(self):
        driver = self.driver
        wait = self.wait
        
        # Enter valid credentials and attempt login
        username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
        password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
        username_field.send_keys("admin")
        password_field.send_keys("Admin123")
        login_button = wait.until(EC.element_to_be_clickable((By.ID, "loginButton")))
        login_button.click()
        
        # Verify login success
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Home')]")))
            print("Login successful!")
        except Exception as e:
            print(f"Login failed! {e}")
            self.fail("Login test failed.")
    
    def test_login_failure(self):
        driver = self.driver
        wait = self.wait
        
        # Enter invalid credentials and attempt login
        username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
        password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
        username_field.send_keys("invalid_user")
        password_field.send_keys("invalid_password")
        login_button = wait.until(EC.element_to_be_clickable((By.ID, "loginButton")))
        login_button.click()
        
        # Verify login failure
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Invalid username or password. Please try again.')]")))
            print("Login failed with an error message as expected!")
        except Exception as e:
            print(f"Expected login failure did not occur! {e}")
            self.fail("Login failure test failed.")
    
    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))

