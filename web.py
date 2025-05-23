from bs4 import BeautifulSoup
import lxml


with open("website.html",encoding='utf-8') as file:
    content=file.read()

soup=BeautifulSoup(content,"html.parser") 

print(soup.title)
section_heading=soup.find(name="h1",id="name")
print(section_heading)

section_heading=soup.find(name="h3",class_="heading")
print(section_heading.get("class"))






