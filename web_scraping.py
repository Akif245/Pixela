from bs4 import BeautifulSoup
import requests


response=requests.get("https://news.ycombinator.com/news")
yc_webpage=response.text

soup=BeautifulSoup(yc_webpage,"html.parser")
# print(soup.title)

links=[]
scores=[]

tag=soup.find_all(class_="titleline")
for tag in tag:
    links.append(tag.a.get("href"))

print(links)
# print(vote.text)


vote=[votes.getText() for votes in soup.find_all(name="span",class_="score")]
scores.append(vote)
print(vote[0].split()[0])

large=max(vote)
index=vote.index(large)
# print(index)


print(links[index])















