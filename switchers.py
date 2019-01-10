def switch_frequency(number1, number2):
    switcher = {
        0: "0",
        1: "1",
        2: "2",
        12: "3",
        10: "4",
        11: "5",
        22: "6",
        21: "7",
        20: "8"
    }
    number = int(str(number1) + str(number2))
    return switcher.get(number)


# R-0 P-1 S-2
def switch_winner(number1, number2):
    switcher = {
        0: "0",
        1: "2",
        2: "1",
        12: "2",
        10: "1",
        11: "0",
        22: "0",
        21: "1",
        20: "2"
    }
    number = int(str(number1) + str(number2))
    return switcher.get(number)


# R-0 P-1 S-2
def getOpposite(number):
    switcher = {
        0: "1",
        1: "2",
        2: "0"
    }
    return switcher.get(number)


def get_move(number):
    number = int(number)
    if number == 0:
        return 'rock'
    elif number == 1:
        return "paper"
    elif number == 2:
        return "scissors"
