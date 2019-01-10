from RPS import RPS as RPS
import random
import switchers

class MyPlayerRandom(RPS):
    def __init__(self):
        RPS.__init__(self)
        self.frequencyTwo = [0]*9

    def setFrequencyTwo(self, now, last):
        position = int(switchers.switch_frequency(last, now))
        self.frequencyTwo[position] = self.frequencyTwo[position] + 1
        # self.dict[position] = ceva + 1
        return self.frequencyTwo[position]

    def move(self):
        number = input("Rock(0), Paper(1) or Scrissors(2)? ")
        self.moves.append(number)
        return number

    def resolve(self):
        self.move()
