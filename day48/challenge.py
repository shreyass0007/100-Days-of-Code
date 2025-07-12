from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize driver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

driver.get("https://secure-retreat-92358.herokuapp.com/")

# Wait for elements to be present
first_name = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "fName"))
)
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")

# Fill out the form
first_name.send_keys("Python")
last_name.send_keys("Programmer")
email.send_keys("python@example.com")

# Submit the form
submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn")
submit_button.click()

# Wait for success message
success = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "alert-success"))
)
print("Form submitted successfully!")

