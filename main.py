import MyPlayerRandom as MyPlayerRandom
import ComputerRandom as ComputerRandom
import ComputerIA as ComputerIA
import MyPlayer as MyPlayer
import switchers

def game(number1, number2):
    winner = int(switchers.switch_winner(number1, number2))
    return winner

def getWinner(computer, player):
    if(computer.getScore() > player.getScore()):
        return "Computer"
    else:
        return "Player"

computerRandom = ComputerRandom.ComputerRandom()
player = MyPlayerRandom.MyPlayerRandom()

for i in range(16):
    computerChoice = computerRandom.move()
    playerChoice = player.move()
    winner = game(computerChoice, playerChoice)
    if (winner == 1):
        computerRandom.scoreUp()
    elif (winner == 2):
        player.scoreUp()

# print(getWinner(computerRandom, player))
# print(player.getScore())
# print(computerRandom.getScore())

player2 = MyPlayer.MyPlayer("Oana")
computerIA = ComputerIA.ComputerIA(player2)

for i in range(16):
    print("\n GAME", i)
    computerChoice = computerIA.move()
    playerChoice = player2.move()
    winner = game(computerChoice, playerChoice)
    if (winner == 1):
        computerIA.scoreUp()
    elif (winner == 2):
        player2.scoreUp()
    print("computer: ", computerChoice)
    print("score:", computerIA.score, " ", player2.score)

print(getWinner(computerIA, player2))


