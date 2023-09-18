from bs4 import BeautifulSoup
import lxml

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "lxml")
# print(soup.title.string)
#
# print(soup.prettify())

all_anchor_tags = soup.findAll(name="a")
# print(all_anchor_tags)

for tag in all_anchor_tags:
    pass
    # print(tag.get("href"))
    # print(tag.getText())

heading = soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText)
# print(section_heading.name)
# print(section_heading.get("class"))

company_url = soup.select_one(selector="p a")
# print(company_url)

angelas_name = soup.select_one(selector="#name")
# print(angelas_name)

headings = soup.select(".heading")
print(headings)

# for head in headings:
#     print(head.getText())