from bs4 import BeautifulSoup
import lxml


with open("day45/bs4-start/bs4-start/website.html") as file:
    contents=file.read()

soup=BeautifulSoup(contents,"html.parser")
print(soup.title.string)
print(soup.prettify())