import MyPlayerRandom as MyPlayerRandom
import ComputerRandom as ComputerRandom
import ComputerIA as ComputerIA
import MyPlayer as MyPlayer
import switchers


def game(number1, number2):
    winner = int(switchers.switch_winner(number1, number2))
    return winner


def get_winner(computer, player):
    if computer.getScore() > player.getScore():
        return "Computer"
    else:
        return "Player"


computerRandom = ComputerRandom.ComputerRandom()
player = MyPlayerRandom.MyPlayerRandom()

for i in range(16):
    print("\n GAME", i)
    computerChoice = computerRandom.move()
    playerChoice = player.move()
    winner = game(computerChoice, playerChoice)
    if winner == 1:
        computerRandom.scoreUp()
    elif winner == 2:
        player.scoreUp()
    print("computer move: ", computerChoice)
    print("score computer vs player:", computerRandom.score, " ", player.score)

print(get_winner(computerRandom, player))

# for i in range(16):
#     computerChoice = computerRandom.move()
#     playerChoice = player.move()
#     winner = game(computerChoice, playerChoice)
#     if winner == 1:
#         computerRandom.scoreUp()
#     elif winner == 2:
#         player.scoreUp()
#
# print(get_winner(computerRandom, player))
# print("Player score:", player.getScore())
# print("Computer score:", computerRandom.getScore())

