from selenium import webdriver
from selenium.webdriver.common.by import By
#keep Chrome browser open after program finisses
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
element = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[1]/a')
print(element.text)
driver.close()