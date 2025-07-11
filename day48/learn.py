from selenium import webdriver
from selenium.webdriver.common.by import By
#keep Chrome browser open after program finisses
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# price_dollar=driver.find_element(By.CLASS_NAME, value="Nx9bqj CxhGGd")
# price_cents=driver.find_element(By.CLASS_NAME,value="a-price-fraction")

# print(f"The price is {price_dollar}.{price_cents}")
# search_bar=driver.find_element(By.NAME,value="q")
# print(search_bar.get_attribute("placeholder"))

# button=driver.find_element(By.ID,value="submit")
# print(button.size)
# documention_link=driver.find_element(By.CSS_SELECTOR,value=".documentation-widget a")
# print(documention_link.text)


event_time=driver.find_elements(By.CSS_SELECTOR,value='.event-widget time')
for time in event_time:
    print(time.text)
event_name=driver.find_elements(By.CSS_SELECTOR,value=".event-widget a")
for name in event_name:
    print(name.text)

driver.quite()