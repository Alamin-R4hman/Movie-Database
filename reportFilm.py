from connectFilm import *


def reports():
    dbCursor.execute("Select * FROM tblfilms WHERE Genre like 'F%'")

    allFilms = dbCursor.fetchall()

    for eachFilm in allFilms:
        print(eachFilm)


if __name__ == "__main__":
    reports()