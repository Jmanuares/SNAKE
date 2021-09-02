

class Player:
    def __init__(self):
        self.score = 0
        self.highscore = 0

    
    def getscore(self):
        return self.score
    
    def setscore(self,score):
        self.score = score
    
    def gethighscore(self):
        file = open("highscore.txt","r")
        self.highscore = file.read()
        if not self.highscore:
            self.highscore=0
        return int(self.highscore)

    def sethighscore(self,score):
        self.highscore = score
        file = open("highscore.txt","w")
        file.write(str(self.highscore))



    def sumarPuntos(self):
        self.score += 1