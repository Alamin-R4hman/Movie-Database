from connectFilm import *


def reportsGenre():
    genre = input("Enter genre: ").title()
    dbCursor.execute(f"SELECT * FROM tblfilms WHERE Genre = '{genre}'")

    allFilms = dbCursor.fetchall()
    if len(allFilms) == 0:
        print("No films found with this genre.")
    else:
        for eachFilm in allFilms:
            print(eachFilm)


if __name__ == "__main__":
    reportsGenre()
