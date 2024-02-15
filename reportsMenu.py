import readFilm, reportFilmGenre, reportFilmYear, reportFilmRating


def reportMenuFile():
  with open("reportsMenu.txt") as reportMenu:
    userReportMenu = reportMenu.read()
  return userReportMenu


def reportMenu():
  option = 0
  optionsList = ["1", "2", "3", "4", "5"]

  userChoice = reportMenuFile()

  while option not in optionsList:
    print(userChoice)

    option = input("Enter an option from the Reports main menu! ")

    if option not in optionsList:
      print(f"{option} is not a valid choice in the Reports menu! ")
  return option


mainReportsProgram = True
while mainReportsProgram:
  mainReportsMenu = reportMenu()

  if mainReportsMenu == "1":
    readFilm.readFilm()
  elif mainReportsMenu == "2":
    reportFilmGenre.reportsGenre()
  elif mainReportsMenu == "3":
    reportFilmYear.reportsYear()
  elif mainReportsMenu == "4":
    reportFilmRating.reportsRating()
  else:
    mainReportsProgram = False

input("Enter to quit the Report on Films App! ")
