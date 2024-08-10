
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path = "chromedriver.exe")
driver = webdriver.Chrome(service = service)

try:
    # Navigate to the login page

    driver.get("https://www.instagram.com/")  

    # Wait until the username field is present
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))  # Adjust selector as needed
    )

    # Enter the username
    username_input = driver.find_element(By.NAME, "username")  # Adjust selector as needed
    username_input.send_keys("deinharddavid@gmail.com")  # Replace with actual username

    # Enter the password
    password_input = driver.find_element(By.NAME, "password")  # Adjust selector as needed
    password_input.send_keys("Vision@2030")  # Replace with actual password

    # Click the login button
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")  # Adjust selector as needed
    login_button.click()

    # Wait for the home page to load and display the welcome message
    welcome_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Welcome')]"))  # Adjust selector as needed
    )

    # Verify the welcome message is displayed
    if welcome_message.is_displayed():
        print("Test passed: User is successfully redirected to the homepage.")
    else:
        print("Test failed: Welcome message not found.")

finally:
    # Close the WebDriver
    driver.quit()
