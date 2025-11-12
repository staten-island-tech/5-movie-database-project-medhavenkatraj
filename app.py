import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)
for index, item in enumerate(data):
    print(item["title"])


    input("do you want to see all the movies after 1900? ").lower()
    for index, item in enumerate(data):
        if item >= 1900:
            print(item["year"]) >= 1900

