from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
#keep Chrome browser open after program finisses
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://duckduckgo.com")
# element = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")

#find element by link text
all_portals=driver.find_element(By.LINK_TEXT,value="Content portals")
# all_portals.click()


#find the  "search"<input> by Name

search = driver.find_element(By.NAME, value="q")
search.send_keys("python",Keys.ENTER)


