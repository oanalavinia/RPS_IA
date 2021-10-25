import ComputerMedium as ComputerMedium
import MyPlayer as MyPlayer
import switchers


def game(number1, number2):
    winner = int(switchers.switch_winner(number1, number2))
    return winner

def test2():
    return "test"

def get_winner(computer, player):
    if computer.getScore() > player.getScore():
        return "Computer"
    else:
        return "Player"


def pretty_print(computer_choise, player_choise):
    print("computer: ", switchers.get_move(computerChoice))
    print("player: ", switchers.get_move(playerChoice))
    print("score computer vs player:", computerMedium.score, " ", player2.score)


player2 = MyPlayer.MyPlayer("Oana")
computerMedium = ComputerMedium.ComputerIA()

name = input("What's your name?")
computerMedium.player = name
computerMedium.get_dictionary()

for i in range(16):
    print("\n GAME", i)
    computerChoice = computerMedium.move()
    playerChoice = player2.move()
    computerMedium.opp_moves.append(playerChoice)
    winner = game(computerChoice, playerChoice)
    if winner == 1:
        computerMedium.scoreUp()
    elif winner == 2:
        player2.scoreUp()
    pretty_print(computerChoice, playerChoice)
    if computerMedium.score == 8 or player2.score == 8:
        break

computerMedium.set_dictionary()
print(get_winner(computerMedium, player2))
