#file 1
import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)
for index, item in enumerate(data):
    print(item["title"])

""" def hello_movies():
    input("do you want to see all the movies after 1900? ").lower()
    for index, item in enumerate(data):
        if item >= 1900:
            print(item["year"]) >= 1900
hello_movies() """


#file 2
def hello_movies():
    year = int(input("enter a year: "))
    print("movies releases after", year, ":" )
    for item in data:
        if item ["year"] > year:
            print(item["title"])
hello_movies()


#file 3 

def hello_movies():
    year = int(input("enter a year: "))
    print("movies released before", year, ":" )
    for item in data:
        if item ["year"] < year:
            print(item["title"])
hello_movies()


#file 4 

def hello_movies():
    year = int(input("enter a year: "))
    print("movies released before", year, ":" )
    for item in data:
        if item ["year"] < year:
            print(item["title"])
hello_movies()


