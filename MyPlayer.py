from RPS import RPS as RPS


class MyPlayer(RPS):
    def __init__(self, name):
        RPS.__init__(self)
        self.frequencyTwo = [0] * 9
        self.name = name

    def move(self):
        number = input("Rock(0), Paper(1) or Scrissors(2)? ")
        while not 0 <= int(number) <= 2:
            number = input("That's not the game. Choose again: ")
        self.moves.append(number)
        return number
