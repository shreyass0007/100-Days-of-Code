import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response=requests.get(URL)
TOP_MOIVES=response.text

soup=BeautifulSoup(TOP_MOIVES,"html.parser")
movie_titles=[]
movie_title=soup.find_all(name="h3",class_="title")

for title in movie_title:
    name=title.get_text()
    movie_titles.append(name)
reversed_list = list(reversed(movie_titles))

with open("movies.txt", "a", encoding="utf-8") as file:  # ✅ Always use UTF-8
    file.write("\n".join(reversed_list))