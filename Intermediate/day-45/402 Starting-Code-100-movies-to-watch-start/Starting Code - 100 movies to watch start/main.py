import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
empire_webpage = response.text
movie_list = []
movie_numbers = []

soup = BeautifulSoup(empire_webpage, "html.parser")
movie_headings = soup.find_all(name="h3", class_="title")

for movie in movie_headings:
    movie_name = movie.getText().split(' ', 1)[1]
    movie_number = movie.getText().split(' ', 1)[0]
    movie_list.append(movie_name)
    movie_numbers.append(movie_number)

# print(len(movie_list))
# print(movie_numbers)
num = len(movie_list)
with open('file.txt', 'w', encoding="utf-8") as file:
    for i in movie_list:
        file.write(f'{movie_numbers[num - 1]} {movie_list[num - 1]}\n')
        num -= 1


# movie_index = movie_headings[0].getText().split(')')[0]
# movie_index_number = movie_headings[0].getText().split(') ')[1]
# print(movie_index)
# print(movie_index_number)

