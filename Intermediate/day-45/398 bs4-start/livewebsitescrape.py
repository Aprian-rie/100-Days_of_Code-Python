from bs4 import BeautifulSoup
import  requests

response = requests.get("https://news.ycombinator.com/")

yc_webpage = (response.text)

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name="span", class_="titleline")

articles_text = []
articles_link = []
list_upvotes = []

for article in articles:
    article_text = article.getText()
    articles_text.append(article_text)
    article_link = article.find(name="a").get("href")
    articles_link.append(article_link)


# article_1_text = article_1.getText()
# article_1_link = article_1.find(name="a").get("href")
# article_1_upvote = soup.find(name="span", class_="score").getText()

article_upvotes = soup.find_all(name="span", class_="score")

for upvote in article_upvotes:
    article_upvote = int(upvote.getText().split()[0])
    list_upvotes.append(article_upvote)


# print(articles_link)
# print(articles_text)
# print(list_upvotes)

highest_upvote = max(list_upvotes)
highest_upvote_index = list_upvotes.index(highest_upvote)
print(highest_upvote_index)
print(articles_text[highest_upvote_index])
print(articles_link[highest_upvote_index])


