class Player:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank

    def getRank(self):
        return self.rank

#en team, se guardará el nombre y el ranking del equipo
class Team:
    def __init__(self, name):
        self.name = name
        self.rank = 0
        self.members = []
        self.lives = 2
    
    def getName(self):
        return self.name

    def getRank(self):
        return self.rank

    def lose(self):
        self.lives -= 1;
    
    def addMember(self,player):
        if len(self.members) < 5:
            self.members.append(player)
    
    def calculateRank(self):
        rank = 0
        for member in self.members:
            rank += member.getRank()
        self.rank = rank / len(self.members)

        
#en bracket estarán 2 objetos tipo Team, correspondiente a cada equipo
class Bracket:

    def __init__(self, team1 = None, team2 = None):
        self.team1 = team1
        self.team2 = team2

    #muestra los equipos del bracket
    def showTeams(self):
        if self.team1 != None and self.team2 != None:
            print(self.team1.getName())    
            print(self.team2.getName())
        elif self.team1 == None and self.team2 != None:     
            print("team1 is null")
        elif self.team1 != None and self.team2 == None:
            print("team2 is null")
        elif self.team1 == None and self.team2 == None:
            print("bracket empty")
        print("-------------------")
    
    def setTeam1(self, team1):
        self.team1 = team1

    def setTeam2(self, team2):
        self.team2 = team2

    def setTeams(self, team1, team2):    
        self.team1 = team1
        self.team2 = team2

    #le das el nombre de un equipo y te devuelve el objeto Team corespondiente
    def getWinner(self, team):
        if team == self.team1.getName():            
            return self.team1
        elif team == self.team2.getName():            
            return self.team2

    #le das el nombre del equipo ganador y te devuelve el perdedor           
    def getLoser(self, team):
        if team == self.team1.getName():            
            return self.team2
        elif team == self.team2.getName():            
            return self.team1
    
    def getTeam1(self):
        return self.team1
    def getTeam2(self):
        return self.team2
    
    def isFull(self):
        if(self.team1 == None or self.team2 == None):
            return False
        else:
            return True


#Este es un poco mas engorroso
#El torneo tiene 2 atributos, una matriz y un entero "fase"
#Fase está relacionado con los "niveles" que tiene el torneo, si son 8 participantes, tiene 3, si son 16, participantes 4 y asi
#Pero representa la fase en la que se encuentra el torneo, siendo 0 el nivel con las primeras partidas
#Para armar la matriz, se recibe la cantidad de equipos y se crea el arbol del torneo con brackets vacios
#si es un torneo de 8 equipos, tournament[0], tendría un arreglo de 4 brackets, tournament[1] tendría uno de 2 y asi
class Tournament:    
    def __init__(self, tournament_size):
        self.winnerSideWinner = None
        self.loserSideWinner = None
        self.tournament_size = tournament_size
        self.fase = 0
        self.loserFase = 0
        self.floors = 0
        self.loserFloors = 0
        self.winner = None
        bracket_size = tournament_size/2
        tournament = []
        while bracket_size >=1:
            self.floors +=1
            bracket = Bracket()
            brackets = []
            for i in range(int(bracket_size)):
                bracket = Bracket()
                brackets.append(bracket)
            tournament.append(brackets)
            bracket_size /= 2
        self.intern = True  
        self.invertion = True           
        loserTournament = []
        while bracket_size >=1:
            self.loserFloors +=1
            bracket = Bracket()
            brackets = []
            for i in range(int(bracket_size)):
                bracket = Bracket()
                brackets.append(bracket)
            loserTournament.append(brackets)
            self.intern = not self.intern
            if not self.intern:
                bracket_size /= 2
        self.loserTournament = loserTournament 
        self.tournament = tournament
        self.newLosers = []

    def getSize(self):
        return self.tournament_size

    def addInitialTeam(self, team):
        i=0
        for bracket in self.tournament[self.fase]:                  
            i+=1
            if bracket.getTeam1() == None:         
                bracket.setTeam1(team)
                return
            elif bracket.getTeam2() == None:
                bracket.setTeam2(team)                    
                return        


    #muestra los brackets en los que se esté
    def showBrackets(self):
        print("FASE: " + str(self.fase))
        print("----- Winner Brackets------")    
        print("--------------------------")    
        for bracket in self.tournament[self.fase]:
            bracket.showTeams()    
        print("----- Loser Bracket------")    
        print("--------------------------")    
        ##for bracket in self.loserTournament[self.loserFase]:
          ##  bracket.showTeams()    
        #wip   
    
    #en este metodo se van pidiendo los resultados de las partidas para ir creando el bracket siguiente
    #la parte de los perdedores aun es wip
    def getWinnerResults(self):
        bracket_position = 0
        print("Getting results of fase " + str(self.fase) + "On winner side")        
        
        for bracket in self.tournament[self.fase]:
            bracket.showTeams()    
            winner = str(input("who is the winner of bracket " + str(bracket_position)+ "? "))            
            self.newLosers.append(bracket.getLoser(winner))
            if self.fase == self.floors:
                self.winnerSideWinner = bracket.getWinner(winner) 
            elif self.tournament[self.fase + 1][bracket_position].getTeam1() == None:                
                self.tournament[self.fase + 1][bracket_position].setTeam1(bracket.getWinner(winner))                                
            elif self.tournament[self.fase + 1][bracket_position].getTeam2() == None:
                self.tournament[self.fase + 1][bracket_position].setTeam2(bracket.getWinner(winner))                
                self.tournament[self.fase +1][bracket_position].showTeams()                            
                bracket_position += 1                    
            else:
                print("no team selected")          

        self.fase += 1
    
    def addLosersToLosersBracket(self):
        if not self.intern:
            if self.invertion:
                bracket = 0 
                losers = list(reversed(self.newLosers))
                for team in losers:
                    self.loserTournament[self.loserFase][bracket].setTeam2(team)                
                    bracket+=1
            if not self.invertion and self.loserFase != 0:
                bracket = 0 
                for team in self.newLosers:
                    if bracket%2 == 0:
                        self.loserTournament[self.loserFase][bracket].setTeam2(team)                
                    bracket+=1
                for team in self.newLosers:
                    if bracket%2 != 0:
                        self.loserTournament[self.loserFase][bracket].setTeam2(team)                
                    bracket+=1
        
    def getLoserResults(self):
        bracket_position = 0
        print("Getting results of fase " + str(self.loserFase) + "On loser side")        
        if not self.intern:
            for bracket in self.loserTournament[self.loserFase]:
                bracket.showTeams()    
                winner = str(input("who is the winner of bracket " + str(bracket_position)+ "? "))                            
                if self.loserFase == self.LoserFloors:
                    self.loserSideWinner = bracket.getWinner(winner) 
                elif self.loserTournament[self.loserFase + 1][bracket_position].getTeam1() == None:                
                    self.loserTournament[self.loserFase + 1][bracket_position].setTeam1(bracket.getWinner(winner))                                
                elif self.loserTournament[self.loserFase + 1][bracket_position].getTeam2() == None:
                    self.loserTournament[self.loserFase + 1][bracket_position].setTeam2(bracket.getWinner(winner))                                    
                    bracket_position += 1                    
                else:
                    print("no team selected")        
        else:
            bracket_position = 0
            for bracket in self.loserTournament[self.loserFase]:
                bracket.showTeams()    
                winner = str(input("who is the winner of bracket " + str(bracket_position)+ "? "))                                            
                self.loserTournament[self.loserFase + 1][bracket_position].setTeam1(bracket.getWinner(winner))
                bracket_position += 1            
        self.loserFase += 1
        self.intern != self.intern


    def checkFullBrackets(self):
        i = 0
        for bracket in self.tournament[self.fase]:
            if bracket.isFull():
                print("Bracket " + str(i)+ " full")
            else:
                if bracket.getTeam1() == None:
                    print("Bracket " + str(i) + " no teamA or teamB")
                elif bracket.getTeam2() == None:
                    print("Bracket " + str(i) + " no teamB")
            i+=1
    def finalMatches(self):
        finalBracket = Bracket(self.winnerSideWinner, self.loserSideWinner)
        finalBracket.showTeams()
        winner = input("who is the winner of final match? ")
        winnerTeam = finalBracket.getWinner(winner)
        if winnerTeam == self.winnerSideWinner:
            self.winner = self.winnerSideWinner

        else:
            winner = input("who is the winner of final re-match? ")
            winnerTeam = finalBracket.getWinner(winner)
            if winnerTeam == self.winnerSideWinner:
                self.winner = self.winnerSideWinner
            elif winnerTeam == self.loserSideWinner:
                self.winner = self.loserSideWinner
        print("the winner is " + winnerTeam.getName())



    def changeFase(self):
        self.fase += 1


    
   

        

            