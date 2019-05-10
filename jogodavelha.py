from random import randint
import numpy as np

def user_moves_first():
    if randint(0,1) == 1:
        return True
    else:
        return False

def create_table_matrix():
    table = np.empty(shape=(3,3), dtype=str)
    return table

def row_and_column_picker():
    valid = False
    while(valid == False):
        user_input = input("Digite: (linha) (coluna)")
        line, column = user_input.split()
        line = int(line)
        column = int(column)
        if(line < 1 or column < 1):
            print("Linhas e colunas só podem ser 1, 2 ou 3.")
        elif(line > 3 or column > 3):
            print("Linhas e colunas só podem ser 1, 2 ou 3.")
        else: 
            valid = True
    return (line-1, column-1) # -1 por conta dos índices da lista

def user_turn(table):
    line_and_column = row_and_column_picker()
    table = mark_table('U', line_and_column[0], line_and_column[1], table)
    print(table)
    return table

def mark_table(player, row, column, table):
    table[row][column] = player
    return table

def is_empty_string(string):
    if not string:
        return True
    else:
        return False

def choose_first_empty(table):
    for i in range(3):
        for j in range(3):
            if is_empty_string(table[i][j]):
                table = mark_table('C', i, j, table)
                return table
    print("Não há mais espaços disponíveis no tabuleiro")
    return table

def computer_turn(table):
    table = choose_first_empty(table)
    print(table)
    return table

def game_flow(first_time, previous_player, table):
    if(first_time == True):
        if(user_moves_first() == True):
            table = user_turn(table)
            table = game_flow(False, 'U', table)
        else:
            table = computer_turn(table)
            table = game_flow(False, 'C', table)
    else:
        if(previous_player == 'C'):
            print("Sua vez!")
            table = user_turn(table)
            table = game_flow(False, 'U', table)
        elif(previous_player == 'U'):
            print("Vez da máquina!")
            table = computer_turn(table)
            table = game_flow(False, 'C', table)
        else:
            print("Ops, algo estranho aconteceu.")
    return table
    
def check_win_conditions(table):
    
    return table

table = create_table_matrix()
print(table)
print(is_empty_string(table[0][0]))
game_flow(True, None, table)