import classes
import functions


orderedRanking = functions.rankTeamList("orderedTeams")
shuffledRanking = functions.rankTeamList("shuffledTeams")
option = int(input("seleccione opcion: 1 - equipo con jugadores similares       2 - equipo con jugadores diversos"))

tournament = None
if option == 1:
    tournament = functions.createTournamentFromRanking(orderedRanking)
elif option == 2:
    tournament = functions.createTournamentFromRanking(shuffledRanking)    

while True:
    option = int(input("seleccione opcion: 1- ingresar resultados de ganadores 2- ingresar resultados del lado de perdedores 3 - mostrar brackets 4 - jugar final"))
    if option ==1:
        tournament.getWinnerResults()
        tournament.addLosersToLosersBracket()
    elif option ==2:
        tournament.getLoserResults()
    elif option ==3:
        tournament.showBrackets()
    elif option == 4:
        tournament.finalMatches()



