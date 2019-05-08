from random import randint
import numpy as np

def user_moves_first():
    if randint(0,1) == 1:
        return True
    else:
        return False

def create_table_matrix():
    table = np.empty(shape=(3,1), dtype=str)
    return table

def column_and_line_picker():
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

def mark_table(player, line, column, table):
    table[line][column] = player
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

def check_stop_conditions(table):
    return table

table = create_table_matrix()
print(table)
print(is_empty_string(table[0][0]))
line_and_column = column_and_line_picker()
table = mark_table('U', line_and_column[0], line_and_column[1], table)
print(table)
table = choose_first_empty(table)
print(table)
table = mark_table('U', line_and_column[2], line_and_column[2], table)
print(table)