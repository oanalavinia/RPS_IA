from RPS import RPS as RPS
import random
import switchers
import os


def get_opponent(move):
    return switchers.getOpposite(move)


def get_max_dictionary(dictionary):
    maxim = 0
    for value in dictionary.values():
        if value > maxim:
            maxim = value
    for move, number in dictionary.items():
        if number == maxim:
            return move


def get_content_by_file_name(file_name):
    path = os.path.join(os.getcwd(), 'dict_med')
    file_path = os.path.join(path, file_name+'.txt')
    if os.path.exists(file_path):
        f = open(file_path, 'r')
        content = f.read()
        f.close()
    else:
        new_file_path = os.path.join(path, file_name+'.txt')
        f = open(new_file_path, 'w')
        content = "0 0 0 0 0 0 0 0 0"
        # g.close()
        f.close()
    return content


class ComputerIA(RPS):
    def __init__(self):
        RPS.__init__(self)
        self.opp_moves = []
        self.player = 'all'
        self.dict_moves = {
            0: 0,
            1: 0,
            2: 0
        }

    def get_dictionary(self):
        content = get_content_by_file_name(self.player)
        allValues = content.split(' ')
        for i in range(3):
            self.dict_moves[i] = int(allValues[i])

    def set_dictionary(self):
        path = os.path.join(os.getcwd(), 'dict_med')
        file_path = os.path.join(path, self.player + '.txt')
        with open(file_path, 'w') as f:
            for i in self.dict_moves:
                f.write(str(self.dict_moves[i]) + ' ')

    def get_move(self):
        if len(self.opp_moves) > 0:
            return self.opp_moves[-1]

    def get_last_move(self):
        if len(self.opp_moves) > 1:
            return self.opp_moves[-2]

    def set_frequency(self, move):
        if move is None:
            return
        move = int(move)
        self.dict_moves[move] = self.dict_moves[move] + 1

    def get_next_move(self):
        # if move is None:
        #     return
        return get_max_dictionary(self.dict_moves)

    def move(self):
        move = self.get_move()
        self.set_frequency(move)
        number = self.get_next_move()
        if number is None:
            return random.choice([0, 1, 2])
        else:
            return get_opponent(number)
