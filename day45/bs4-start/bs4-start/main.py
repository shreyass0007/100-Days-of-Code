from bs4 import BeautifulSoup
import requests
response=requests.get("https://appbrewery.github.io/news.ycombinator.com/")

yc_web_page=response.text

soup=BeautifulSoup(yc_web_page,"html.parser")


articles=soup.find_all(name="a",class_="storylink")
article_texts=[]
article_links=[]
article_upvotes=[]
for artical_tag in articles:
    text=artical_tag.getText()
    article_texts.append(text)
    link=artical_tag.get("href")
    article_links.append(link)
article_upvote=soup.find_all(name="span",class_="score")

print(article_texts)
print(article_links)
for score in article_upvote:
    upvotes=(int(score.getText().split(" ")[0]))
    article_upvotes.append(upvotes)

max_value=max(article_upvotes)
max_index=article_upvotes.index(max_value)
print(article_texts[max_index])
print(article_links[max_index])
print(article_upvotes[max_index])