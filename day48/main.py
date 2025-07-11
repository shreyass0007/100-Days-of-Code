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
search_bar=driver.find_element(By.NAME,value="q")
print(search_bar.get_attribute("placeholder"))

button=driver.find_element(By.ID,value="submit")
print(button.size)
# driver.close()
driver.quit()