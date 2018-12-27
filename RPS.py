class RPS:
    def __init__(self):
        self.frequency = [0]*3
        self.moves = []
        self.choices = [0,1,2]
        self.score = 0

    def scoreUp(self):
        self.score = self.score+1

    def getScore(self):
        return self.score

    def prettyPrint(self):
        print(self.moves)
        print(self.score)
