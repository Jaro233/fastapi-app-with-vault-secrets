import time

import chromedriver_autoinstaller

# from get_chrome_driver import GetChromeDriver
from httpcore import TimeoutException
from pyvirtualdisplay import Display

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

display = Display(visible=0, size=(800, 800))
display.start()

chromedriver_autoinstaller.install()

chrome_options = webdriver.ChromeOptions()
# Add your options as needed
options = [
    # Define window size here
    "--window-size=1200,1200",
    "--ignore-certificate-errors",
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage",
    "--remote-debugging-port=9222",
]

for option in options:
    chrome_options.add_argument(option)


driver = webdriver.Chrome(options=chrome_options)

driver.get(
    "http://localhost:8000/add-book"
)  # Adjust the URL to where your app is hosted

# Assume the form fields have 'name' attributes: title, author, genre, status, user_rating
title = driver.find_element(By.ID, "title")
author = driver.find_element(By.ID, "author")
genre = driver.find_element(By.ID, "genre")
status = driver.find_element(By.ID, "status")
user_rating = driver.find_element(By.ID, "user_rating")

# Fill out the form
title.send_keys("Selenium Test Book")
author.send_keys("Selenium Tester")
genre.send_keys("Testing")
status.send_keys("to read")
user_rating.send_keys("5")

# Assume the submit button has an xpath
submit_button = driver.find_element(By.XPATH, "//button[contains(text(),'Add Book')]")
submit_button.click()

time.sleep(3)

try:
    # Wait for the alert to be present
    WebDriverWait(driver, 10).until(EC.alert_is_present())

    # Switch to the alert
    alert = driver.switch_to.alert

    # Check if the alert text is what we expect
    if alert.text == "Book added successfully":
        print("Alert message confirmed:", alert.text)
        # Accept the alert (click OK)
        alert.accept()
    else:
        print("Alert message was not as expected. Actual message:", alert.text)
        # Optionally, handle the unexpected alert text here
        alert.dismiss()  # or alert.accept() depending on the desired action
        assert False, "The alert message was not as expected."

except TimeoutException:
    print("No alert was present after 10 seconds.")
    assert False, "No alert appeared within the expected time."

driver.quit()
