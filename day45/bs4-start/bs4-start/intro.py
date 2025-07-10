from bs4 import BeautifulSoup
import lxml


with open("day45/bs4-start/bs4-start/website.html") as file:
    contents=file.read()

soup=BeautifulSoup(contents,"html.parser")
print(soup.title.string)
# print(soup.prettify())
all_anchor_tags=soup.find(name="p")

# for tag in all_anchor_tags:
#     print(tag.get("href"))


heading=soup.find(name="h1",id="name")
print(heading.get_text())

section_heading=soup.find(name="h3",class_="heading")
print(section_heading.get("class"))


print(soup.select(".heading"))