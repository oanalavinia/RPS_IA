from RPS import RPS as RPS


class MyPlayer(RPS):
    def __init__(self, name):
        RPS.__init__(self)
        self.frequencyTwo = [0] * 9
        self.name = name

    def move(self):
        number = input("Rock(0), Paper(1) or Scrissors(2)? ")
        self.moves.append(number)
        return number
