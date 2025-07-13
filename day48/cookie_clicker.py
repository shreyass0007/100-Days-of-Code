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

try:
    driver.get("https://orteil.dashnet.org/cookieclicker/")
    
    # Wait for and click the language selection button
    lang_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.langSelectButton'))
    )
    lang_button.click()
    
    # Wait for game to load after language selection
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'bigCookie'))
    )
    
    print("Game loaded successfully! Ready for automation.")
    
except Exception as e:
    print(f"Error occurred: {e}")