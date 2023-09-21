Day 45
### learning how to scrape the web for Data Using Beautiful soup
Web Scraping involves looking through the underlying HTML code of a website to get hold of the information that we want.

<p align="center"><img src="web_scraping.png" width="300" /></p>

The aim for today is to learn how to make soup using beautiful soup!


Beautiful soup is a module that helps developers make sense of websites and pull out the relevant parts of the data.
It is basically a HTMl parser.

### Parsing HTML and Making Soup
This is the first step to extracting the data contained in a website.
```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(contents, 'html.parser')
# The first argument is the websites content
# The second argument is the parser as it is going to help the 
# beautiful soup module understand what language the particular content is structured in.
# as beautiful soup can parse HTML and XML
```
Depending on the website we might have to use the lxml parser
```python
from  bs4 import BeautifulSoup
import lxml
# The code is preety much the same except in the parser
soup = BeautifulSoup(contents, 'lxml')
```
Beautiful soup documentation: {linkkk}
<p align="center"><img src="beautiful_soup.png" width="300" /></p>

### Finding and Selecting Particular Elements with Beautiful Soup
The soup is now an object that allows us to tap in to various parts of the website
Consider the html website below
```html
<!DOCTYPE html>
<html>

<head>
	<meta charset="utf-8">
	<title>Aprian's Personal Site</title>
</head>

<body>
	<h1 id="name">Aprian Rie</h1>
	<p><em>Founder of <strong><a href="https://www.rie.co/">The App Brewery</a></strong>.</em></p>
	<p>I am a full stack developer.</p>
	<hr>
	<h3 class="heading">Languages I know</h3>
	<ul>
		<li>Python</li>
		<li>Java</li>
		<li>Dart (Flutter)</li>
	</ul>
	<hr>
	<h3 class="heading">Other Pages</h3>
	<a href="https://aprian.github.io/cv/hobbies.html">My Hobbies</a>
	<a href="https://aprian.github.io/cv/contact-me.html">Contact Me</a>
</body>

</html>
```
If I wanted to extract the title tag from the html website above
```python
title_tag = soup.title
print(title_tag)
# The code above prints out the entire title tag
```
#### Output
``<title>Aprian's Personal Site</title>``

We can also get hold of other things like name of the tag and the String contained in the title tag
```python
print(soup.title.name)
# Prints out the name of the particular title tag

print(soup.title.string)
# Prints out the String inside the title tag
```

#### Output
``title``


``Aprian's Personal Site``

In addition to getting the title tag, we can also get hold of different tags that are present in the website
For instance the a tag
```python
print(soup.a)
# Gives us the first anchor tag that it finds in our website
# In this case it will be <a href="https://www.rie.co/">The App Brewery</a>
```
#### Output
``<a href="https://www.rie.co/">Rie's Site</a>``

Other elements also can be used such as

``soup.li``
``soup.p``

### Finding and Selecting All Elements With Beautiful soup
What if we wanted all the paragraphs or all anchor tags in our website

So to search the website for all the components that we're looking for we can use a function called ``find_all``

We can search for many things such as by name

```python
all_anchor_tags = soup.find_all(name='a')
print(all_anchor_tags)
# It is going to give us all the anchor tags present in the website as a list
# Since it prints a list of all anchor tags, to want the strings inside the tags a for loop is used

for tag in all_anchor_tags:
    print(tag.getText())

# Also if you wanted to get a hold of the href's
for tag in all_anchor_tags:
    print(tag.get("href"))

# Finding the values by attributes
heading = soup.find(name="h1", id="name")
print(heading)
# This prints out my heading because it finds the h1 element with the id name

section_heading = soup.find_all(name="h3", class_="heading")
print(section_heading)
# This prints out the heading of the h3 element with class heading
# and class_ has been used instead of class as class is a predefined word in the python language
```
#### Output
``[<a href="https://www.rie.co/">The App Brewery</a>, <a href="https://aprian.github.io/cv/hobbies.html">My Hobbies</a>, <a href="https://aprian.github.io/cv/contact-me.html">Contact Me</a>]``


### Scraping a Live Website

The website used for our case study is the <a href="https://news.ycombinator.com/news">YCombinator's Hacker</a>

This is where anybody can post a link to a news piece that they have discovered that's tech related

```python
from bs4 import BeautifulSoup
import requests
# In order to download the data from the website I uesd the requests

response = requests.get('https://news.ycombinator.com/news')
ycwebpage = response.text
print(ycwebpage)
# the above print statement prints out our webpage in html format (not necessary though)

soup = BeautifulSoup(ycwebpage, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
# Finds all article titles  and stores them in a list of span elements


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


```


- The first basic task that I'll be doing is obtaining data from the website Empire's 100 Greatest Movies of all time. It's a huge list of good movies that everyone should have watched at a certain point of time in their lives.
    
    We are gonna pull out the relevant parts to us namely the title and the ranking of each movieand use it to compile a list of movies that we have to watch so that we can look at the list of the 100 movies.

The code is shown in the file Starting Code - 100-movies-to-watch

## The End