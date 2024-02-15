from connectFilm import *


def reportsRating():
    rating = input("Enter rating: ").title
    dbCursor.execute(f"Select * FROM tblfilms WHERE rating like '{rating}'")

    allFilms = dbCursor.fetchall()
    if len(allFilms) == 0:
        print("No films found with this rating.")
    else:
        for eachFilm in allFilms:
            print(eachFilm)


if __name__ == "__main__":
    reportsRating()
