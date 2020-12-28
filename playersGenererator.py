
#el objetivo de este script es crear un dataset para probar la solución

import random
players = []

#cantidad de jugadores correspondiente a cada categoría segun las estadisticas
iron = int(round(80 * 0.048))
bronze = int(round(80 * 0.2132))
silver = int(round(80 * 0.3414))
gold = int(round(80 * 0.2781))
plat = int(round(80 * 0.1003))
diamond = int(round(80 * 0.0212))

#se generan 80 jugadores con las proporciones correspondientes
p = 0
for i in range(iron):
    name = "player" + str(p)
    mmr = random.randint(0,509) 
    player = []
    player.append(name)   
    player.append(mmr)
    players.append(player)
    p +=1

for i in range(bronze):
    name = "player" + str(p)
    mmr = random.randint(510,1089) 
    player = []
    player.append(name)   
    player.append(mmr)
    players.append(player)
    p +=1

for i in range(silver):
    name = "player" + str(p)
    mmr = random.randint(1090,1409) 
    player = []
    player.append(name)   
    player.append(mmr)
    players.append(player)
    p +=1

for i in range(gold):
    name = "player" + str(p)
    mmr = random.randint(1410, 1719) 
    player = []
    player.append(name)   
    player.append(mmr)
    players.append(player)
    p +=1

for i in range(plat):
    name = "player" + str(p)
    mmr = random.randint(1720,2019) 
    player = []
    player.append(name)   
    player.append(mmr)
    players.append(player)
    p +=1

for i in range(diamond):
    name = "player" + str(p)
    mmr = random.randint(2030, 2330) 
    player = []
    player.append(name)   
    player.append(mmr)
    players.append(player)
    p +=1


#se generan  equipos con miembros del mismo nivel

teams = open("orderedTeams", "w+")
i=0
teamNum = 0
for player in players:
    if i%5== 0:        
        teams.write("team" + str(teamNum) + "\n")
        teamNum +=1 
    teams.write(player[0] + "|" + str(player[1]) + "\n")
    i+=1

#se generan equipos con miembro de distintos niveles
teams = open("shuffledTeams", "w+")
i=0
teamNum = 0
random.shuffle(players)
for player in players:
    if i%5== 0:        
        teams.write("team" + str(teamNum) + "\n")
        teamNum +=1 
    teams.write(player[0] + "|" + str(player[1]) + "\n")
    i+=1





    


