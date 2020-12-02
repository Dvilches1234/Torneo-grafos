#en team, se guardará el nombre y el ranking del equipo
class Team:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank
    
    def getName(self):
        return self.name

#en bracket estarán 2 objetos tipo Team, correspondiente a cada equipo
class Bracket:

    def __init__(self, team1 = None, team2 = None):
        self.team1 = team1
        self.team2 = team2

    #muestra los equipos del bracket
    def showTeams(self):
        print(self.team1.getName())    
        print(self.team2.getName())
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
    
    def getTeam1(self):
        return self.team1
    def getTeam2(self):
        return self.team2

#Este es un poco mas engorroso
#El torneo tiene 2 atributos, una matriz y un entero "fase"
#Fase está relacionado con los "niveles" que tiene el torneo, si son 8 participantes, tiene 3, si son 16, participantes 4 y asi
#Pero representa la fase en la que se encuentra el torneo, siendo 0 el nivel con las primeras partidas
#Para armar la matriz, se recibe la cantidad de equipos y se crea el arbol del torneo con brackets vacios
#si es un torneo de 8 equipos, tournament[0], tendría un arreglo de 4 brackets, tournament[1] tendría uno de 2 y asi
class Tournament:    
    def __init__(self, tournament_size):
        bracket_size = tournament_size/2
        tournament = []
        while bracket_size >1:
            bracket = Bracket()
            brackets = [bracket] * bracket_size
            tournament.append(brackets)
            bracket_size /= 2
        self.tournament = tournament
        self.fase = 0
    
    #funcion para rellenar los brackets iniciales
    def addInitialBracket(self, team1, team2):
        for bracket in self.tournament:
            if bracket.getTeam1() == None and bracket.getTeam2() == None:
                bracket.setTeams(team1, team2)
                break

    #muestra los brackets en los que se esté
    def showBrackets(self):
        print("----- Winner Brackets------")    
        print("--------------------------")    
        for bracket in self.tournament[self.fase]:
            bracket.showTeams()    
        print("----- Loser Bracket------")    
        print("--------------------------")    
        #wip   
    
    #en este metodo se van pidiendo los resultados de las partidas para ir creando el bracket siguiente
    #la parte de los perdedores aun es wip
    def getResults(self):
        next_bracket_position = 0
        for bracket in self.tournament[self.fase]:
            bracket.showTeams()    
            winner = input("who is the winner? ")
            if self.tournament[self.fase + 1][next_bracket_position].getTeam1 == None:
                self.tournament[self.fase + 1][next_bracket_position].setTeam1(bracket.getWinner(winner))
            elif self.tournament[self.fase + 1][next_bracket_position].getTeam2 == None:
                self.tournament[self.fase + 1][next_bracket_position].setTeam2(bracket.getWinner(winner))
                next_bracket_position += 1


    
   

        

            