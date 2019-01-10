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
    path = os.path.join(os.getcwd(), 'dict')
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
        self.dict_rock = {
            0: 0,
            1: 0,
            2: 0
        }
        self.dict_paper = {
            0: 0,
            1: 0,
            2: 0
        }
        self.dict_scissors = {
            0: 0,
            1: 0,
            2: 0
        }

    def get_dictionaries(self):
        content = get_content_by_file_name(self.player)
        allValues = content.split(' ')
        for i in range(3):
            self.dict_rock[i] = int(allValues[i])
            self.dict_paper[i] = int(allValues[i+3])
            self.dict_scissors[i] = int(allValues[i+3])

    def set_dictionaries(self):
        path = os.path.join(os.getcwd(), 'dict')
        file_path = os.path.join(path, self.player + '.txt')
        with open(file_path, 'w') as f:
            for i in self.dict_rock:
                f.write(str(self.dict_rock[i]) + ' ')
            for i in self.dict_paper:
                f.write(str(self.dict_paper[i]) + ' ')
            for i in self.dict_scissors:
                f.write(str(self.dict_scissors[i]) + ' ')


    def get_move(self):
        if len(self.opp_moves) > 0:
            return self.opp_moves[-1]

    def get_last_move(self):
        if len(self.opp_moves) > 1:
            return self.opp_moves[-2]

    def set_frequency(self, move, last_move):
        if last_move is None or move is None:
            return
        move = int(move)
        last_move = int(last_move)
        if last_move == 0:
            self.dict_rock[move] = self.dict_rock[move] + 1
        elif last_move == 1:
            self.dict_paper[move] = self.dict_paper[move] + 1
        elif last_move == 2:
            self.dict_scissors[move] = self.dict_scissors[move] + 1

    def get_next_move(self, move):
        if move is None:
            return
        if int(move) == 0:
            return get_max_dictionary(self.dict_rock)
        elif int(move) == 1:
            return get_max_dictionary(self.dict_paper)
        elif int(move) == 2:
            return get_max_dictionary(self.dict_scissors)

    def move(self):
        move = self.get_move()
        last_move = self.get_last_move()
        self.set_frequency(move, last_move)
        number = self.get_next_move(move)
        if number is None:
            return random.choice([0, 1, 2])
        else:
            return get_opponent(number)
