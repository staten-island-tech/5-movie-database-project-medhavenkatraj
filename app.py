
""" def hello_movies():
    input("do you want to see all the movies after 1900? ").lower()
    for index, item in enumerate(data):
        if item >= 1900:
            print(item["year"]) >= 1900
hello_movies() """


#file 1
""" import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)
for index, item in enumerate(data):
    print(item["title"])


#file 2
def hello_movies():
    year = int(input("enter a year, i will print all the movies releases after that year: "))
    print("movies releases after", year, ":" )
    for item in data:
        if item ["year"] > year:
            print(item["title"])
hello_movies()


#file 3 

def hello_movies():
    year = int(input("enter a year, i will print all the movies releases after that year: "))
    print("movies releases after", year, ":" )
    for item in data:
        if item ["year"] > year:
            print(item["title"])
hello_movies()
def hello_movies():
    year = int(input("enter a year, i will print all the movies released before that year: "))
    print("movies released before", year, ":" )
    for item in data:
        if item ["year"] < year:
            print(item["title"])
hello_movies()


#file 4 

def hello_movies():
    year = int(input("enter a year, i will print all the movies released before that year: "))
    print("movies released before", year, ":" )
    for item in data:
        if item ["year"] < year:
            print(item["title"])
hello_movies()
 """

#file 5

""" import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)
def hello_movies():
    answer = input("pick a movie you want to watch ")
    for item in data:
        print(item["title"])
hello_movies() """

#file 6 

import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)
""" def hello_movies():
    answer = input("search for a genre you would like to watch ")
    for item in data:
        if data == answer:
            print(item["genres"])
hello_movies() """


genres = []
def hello_movies():
    answer = input("enter a genre i will print all relating genres of movies ")
    for item in data:
        if item ["genres"] == genres:
            print(item["title"])
hello_movies()