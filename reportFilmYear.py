from connectFilm import *


def reportsYear():
    year = int(input("Enter year: "))
    dbCursor.execute(f"Select * FROM tblfilms WHERE yearReleased = '{year}'")

    allFilms = dbCursor.fetchall()
    if len(allFilms) == 0:
        print("No films found for this year.")
    else:
        for eachFilm in allFilms:
            print(eachFilm)


if __name__ == "__main__":
    reportsYear()
