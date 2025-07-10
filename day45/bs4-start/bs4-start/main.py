from bs4 import BeautifulSoup
import requests
response=requests.get("https://appbrewery.github.io/news.ycombinator.com/")

yc_web_page=response.text

soup=BeautifulSoup(yc_web_page,"html.parser")
print(soup.title)

article_tag=soup.find(name="a",class_="storylink")
article_link=soup.find(name="a")
article_upvote=soup.find(name="span",class_="score",id="score_40725924")
print(article_tag.get_text())
print(article_link.get("href"))
print(article_upvote.get_text())