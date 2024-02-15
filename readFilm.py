from connectFilm import *


def readFilm():
    dbCursor.execute("Select * from tblfilms")

    allFilms = dbCursor.fetchall()

    for eachFilm in allFilms:
        print(eachFilm)


if __name__ == "__main__":
    readFilm()
