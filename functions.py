import classes
#se supone que aqui leeria el archivo participants y crearia los brackets iniciales
#pero tambien esta wip
def rankTeamList(teamFile):
    ranking = []
    teams = open(teamFile, "r")
    teamNumber = -1
    for line in teams:
        if "|" not in line:            
            if teamNumber >= 0:
                ranking[teamNumber][0].calculateRank()
                ranking[teamNumber][1] = ranking[teamNumber][0].getRank()
            team = classes.Team(line)
            teamData = [team, 0]
            ranking.append(teamData)
            teamNumber +=1
        else:
            playerData = line.split("|")
            player = classes.Player(playerData[0], int(playerData[1]))
            ranking[teamNumber][0].addMember(player)

    ranking[teamNumber][0].calculateRank()
    ranking[teamNumber][1] = ranking[teamNumber][0].getRank()

    return sorted(ranking, key = lambda tup:tup[1])
            
def createTournamentFromRanking(ranking):
    tournament = classes.Tournament(int(len(ranking)))
    middle = len(ranking)//2
    firstHalf = ranking[:middle]
    secondHalf = ranking[middle:]
    for i in range(middle):
        tournament.addInitialTeam(firstHalf[i][0])
        tournament.addInitialTeam(secondHalf[i][0])
    return tournament



             







