from RPS import RPS as RPS
import random
import switchers

class ComputerIA(RPS):
    def __init__(self, MyPlayer):
        RPS.__init__(self)
        self.MyPlayer = MyPlayer
        self.frequency = [0]*9
        self.dict_rock = {
            0: 0,
            1: 0,
            2: 0
        }
        self.dict_paper = {
            0: 0,
            1: 0,
            2: 0
        }
        self.dict_scissors = {
            0: 0,
            1: 0,
            2: 0
        }

    def getMostFrequent(self):
        maxim = max(self.MyPlayer.frequencyTwo)
        mostFrequent = [i for i, j in enumerate(self.MyPlayer.frequencyTwo) if j == maxim]
        if len(mostFrequent)>1:
            return random.choice(mostFrequent)
        return mostFrequent[0]

    def getOpponent(self, move):
        return switchers.getOpposite(move)

    def getMove(self):
        if len(self.MyPlayer.moves) > 0:
            return self.MyPlayer.moves[-1]

    def getLastMove(self):
        if len(self.MyPlayer.moves) > 1:
            return self.MyPlayer.moves[-2]

    def setFrequencyDict(self, move, last_move):
        if last_move is None or move is None:
            return
        move = int(move)
        last_move = int(last_move)
        if last_move == 0:
            self.dict_rock[move] = self.dict_rock[move] + 1
        elif last_move == 1:
            self.dict_paper[move] = self.dict_paper[move] + 1
        elif last_move == 2:
            self.dict_scissors[move] = self.dict_scissors[move] + 1

    def getNextMove(self, move):
        if move is None:
            return
        if int(move) == 0:
            return self.getMaxOfDictionaty(self.dict_rock)
        elif int(move) == 1:
            return self.getMaxOfDictionaty(self.dict_paper)
        elif int(move) == 2:
            return self.getMaxOfDictionaty(self.dict_scissors)

    def getMaxOfDictionaty(self, dictionary):
        max = 0
        for value in dictionary.values():
            if value > max:
                max = value
        for move, number in dictionary.items():
            if number == max:
                return move

    def move(self):
        move = self.getMove()
        last_move = self.getLastMove()
        self.setFrequencyDict(move, last_move)
        number = self.getNextMove(move)
        if number is None:
            return random.choice([0,1,2])
        else:
            return self.getOpponent(number)
