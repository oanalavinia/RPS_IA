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
        number = random.choice(self.choices)
        self.moves.append(number)
        self.frequency[number] = self.frequency[number]+1
        if (len(self.moves)>1):
            self.setFrequencyTwo(number, self.moves[-2])
        return number

    def resolve(self):
        self.move()
