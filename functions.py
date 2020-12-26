import classes

#se supone que aqui leeria el archivo participants y crearia los brackets iniciales
#pero tambien esta wip



def createTournament(contestantsFile):
    contestants =open(contestantsFile, "r")
    tournamentSize = contestants.readline()
    tournament = classes.Tournament(int(tournamentSize)) 
    for line in contestants:
        newline = line.split("|")
        name = newline[0]
        rank = newline[1]
        team = classes.Team(name, rank)
        print("gonna add: " + team.getName())
        tournament.checkFullBrackets()
        tournament.addInitialTeam(team)
    return tournament


tournament = createTournament("participants")
tournament.showBrackets()
tournament.getResults()
tournament.showBrackets()
tournament.getResults()
tournament.showBrackets()
tournament.getResults()
tournament.showBrackets()

             







