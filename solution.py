import classes
import functions


orderedRanking = functions.rankTeamList("orderedTeams")
shuffleddRanking = functions.rankTeamList("shuffledTeams")
option = int(input("seleccione opcion: 1 - equipo con jugadores similares       2 - equipo con jugadores diversos"))
if option == 1:
    tournament = functions.createTournamentFromRanking(orderedRanking)
    size = tournament.getSize()
    while size >=1:
        tournament.showBrackets()
        tournament.getResults()

elif option == 2:
    tournament = functions.createTournamentFromRanking(shuffledRanking)
    size = tournament.getSize()
    while size >=1:
        tournament.showBrackets()
        tournament.getResults()
