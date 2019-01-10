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

def pretty_print(computer_choise, player_choise):
    print("computer: ", switchers.get_move(computerChoice))
    print("player: ", switchers.get_move(playerChoice))
    print("score computer vs player:", computerIA.score, " ", player2.score)



player2 = MyPlayer.MyPlayer("Oana")
computerIA = ComputerIA.ComputerIA()

name = input("What's your name?")
computerIA.player = name
computerIA.get_dictionaries()

for i in range(16):
    print("\n GAME", i)
    computerChoice = computerIA.move()
    playerChoice = player2.move()
    computerIA.opp_moves.append(playerChoice)
    winner = game(computerChoice, playerChoice)
    if winner == 1:
        computerIA.scoreUp()
    elif winner == 2:
        player2.scoreUp()
    pretty_print(computerChoice, playerChoice)
    if computerIA.score == 8 or player2.score == 8:
        break

computerIA.set_dictionaries()
print(get_winner(computerIA, player2))
