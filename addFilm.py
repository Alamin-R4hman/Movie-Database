from connectFilm import *


def createFilm():
    title = input("Enter the film Title: ")
    yearReleased = input("Enter the film Release Year: ")
    rating = input("Enter the film Rating: ")
    duration = input("Enter the film Duration: ")
    genre = input("Enter the film Genre: ")

    dbCursor.execute(
        "INSERT INTO tblfilms(Title, YearReleased, Rating, Duration, Genre) VALUES(?,?,?,?,?)",
        (title, yearReleased, rating, duration, genre),
    )

    dbCon.commit()

    print(f"{title} has been added to you Film records")


if __name__ == "__main__":
    createFilm()
