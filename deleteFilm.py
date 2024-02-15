from connectFilm import *


def deleteFilm():
    idField = input("Enter the Film Id of the Movie you wish to delete:  ")

    dbCursor.execute(f"DELETE FROM tblfilms WHERE filmId = {idField}")

    dbCon.commit()

    print(f"Film number: {idField}  was deleted from the Movie list")


if __name__ == "__main__":
    deleteFilm()
