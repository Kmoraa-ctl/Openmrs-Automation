
# Check for an error message
try:
    error_message = driver.find_element(By.XPATH, "//span[contains(text(), 'Invalid username or password. Please try again.')]")
    print("Login failed with an error message!")
except:
    try:
        driver.find_element(By.XPATH, "//span[contains(text(), 'Home')]")
        print("Login successful!")
    except:
        print("Invalid username or password!")
