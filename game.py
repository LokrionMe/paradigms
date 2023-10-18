import random


def check_string(game_dict, icon):
    for i in range(1, 8, 3):
        if game_dict[i] == icon and game_dict[i+1] == icon and game_dict[i+2] == icon:
            return True
    return False


def check_column(game_dict, icon):
    for i in range(1, 4):
        if game_dict[i] == icon and game_dict[i+3] == icon and game_dict[i+6] == icon:
            return True
    return False


def check_diagonal(game_dict, icon):
    k = 4
    for i in range(1, 4, 2):
        if game_dict[i] == icon and game_dict[i+k] == icon and game_dict[i+k*2] == icon:
            return True
        k /= 2
    return False


def check_result(players_icon, game_dict):
    k = 1
    for icon in players_icon:
        if check_string(game_dict, icon) or check_column(game_dict, icon) or check_diagonal(game_dict, icon):
            return f'{k} player win'
        k += 1
    return False


def check_num(min_val, max_val):
    while True:
        try:
            num_init = int(
                input(f'Input integer number from {min_val} to {max_val}: '))
        except ValueError:
            print("It's must be number")
        else:
            if min_val <= num_init <= max_val:
                return num_init
                break
            print(f'Number must be from {min_val} to {max_val}')


def print_table(game_dict):
    print('\n-------')
    for j in range(1, 8, 3):
        print(
            f'|{game_dict[j]}|{game_dict[j+1]}|{game_dict[j+2]}|', end='\n-------\n')
    print()


def start_game():
    game_dict = {a: a for a in range(1, 10)}
    hod = random.randint(0, 1)
    players_icon = ['X', 'O']
    first_player = players_icon[0]
    second_player = players_icon[1]
    print(f'1st player -> {first_player} \n2nd player -> {second_player}')
    for i in range(10):
        print_table(game_dict)
        checked_result = check_result(players_icon, game_dict)
        if checked_result == False:
            if hod:
                print('1 player turn: ')
                hod -= 1
            else:
                print('2 player turn: ')
                hod += 1
            while True:
                try:
                    pos_of_turn = check_num(1, 9)
                finally:
                    if game_dict[pos_of_turn] == pos_of_turn:
                        game_dict[pos_of_turn] = players_icon[hod]
                        break
                print("This cell is full")
        elif checked_result:
            return checked_result
        if i == 9:
            return "It's draw"


print(start_game())
