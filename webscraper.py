import requests as rq
from bs4 import BeautifulSoup as bs

url="https://edition.cnn.com/travel/article/india-dance/index.html"
response=rq.get(url)
if response.status_code==200:
    s=bs(response.text,'html.parser')
    title=s.find("h1",class_="headline__text inline-placeholder").text
    content=""
    article_body=s.find("div",class_="article__content")
    para=article_body.find_all("p")
    for pa in para:
        content+=pa.text + "\n"
    author=s.find("span",class_="byline__name").text
    Date=s.find("div",class_="timestamp").text

    print("Title of the Article: ",title)
    print("\nAuthor of the Article: ",author)
    print("\nDate of the Article: ",Date)
    print("\nContent: ")
    print(content)
else:
    print("Failed to retrieve the webpage. Status code: ",response.status_code)
