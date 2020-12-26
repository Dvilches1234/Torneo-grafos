import random
par = open("players", "w+")
for i in range(80):
    name = "p"+str(i)
    rank = random.randint(1,20)
    par.write(name + "|" + str(rank) + "\n")
