from bs4 import BeautifulSoup
import requests
response=requests.get("https://appbrewery.github.io/news.ycombinator.com/")

yc_web_page=response.text

soup=BeautifulSoup(yc_web_page,"html.parser")
print(soup.title)