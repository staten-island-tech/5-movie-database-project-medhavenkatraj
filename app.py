import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)
for index, item in enumerate(data):
    print(item["title"])

user = input("pick a movie! type in a year ranging from 1961 to 2023! i will print all the movies after that year ")
if input != 1900:
    print("movies")

