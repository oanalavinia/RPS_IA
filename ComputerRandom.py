from RPS import RPS as RPS
import random

class ComputerRandom(RPS):
    def __init__(self):
        RPS.__init__(self)

    def move(self):
        number = random.choice(self.choices)
        self.moves.append(number)
        self.frequency[number] = self.frequency[number] + 1
        return number
