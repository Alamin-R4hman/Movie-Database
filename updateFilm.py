from connectFilm import *


def updateFilm():
    idField = input("Enter the Film Id of the movie you would like to update: ")
    fieldName = input(
        "Enter Title, YearReleased, Rating, Duration or Genre of the field you would like to alter: "
    ).title()
    fieldValue = input(f"Enter the value for {fieldName} field: ")
    fieldValue = "'" + fieldValue + "'"

    dbCursor.execute(
        f"UPDATE tblfilms SET {fieldName} = {fieldValue} WHERE filmId = {idField} "
    )

    dbCon.commit()
    print(f"Film {idField} {fieldName} has been updated in the Movie list. ")


if __name__ == "__main__":
    updateFilm()
