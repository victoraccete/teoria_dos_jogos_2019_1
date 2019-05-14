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
    return (line-1, column-1) # -1 por conta dos índices da matriz

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
    return table

def is_there_empty_space(table):
    empty_space = False
    for i in range(3):
        for j in range(3):
            if is_empty_string(table[i][j]):
                empty_space = True
    return empty_space

def computer_turn(table):
    positions = check_if_about_to_win_by_rows(table)
    if(positions == None):
        positions = check_if_about_to_win_by_columns(table)
    if(positions == None):
        positions = check_if_about_to_win_by_diagonals(table)        
    
    if(positions == None):
        table = choose_first_empty(table)
        print(table)
        return table
    else:
        print("Alguém prestes a ganhar em: ")
        print(positions[0], positions[1])
        table = mark_table('C', positions[0], positions[1], table)
        print(table)
        return table
    return table
        

def game_flow(first_time, previous_player, table):
    if(check_win_conditions(table) == True):
        print("Jogo encerrado!")
        return table
    elif(is_there_empty_space(table) == False):
        print("Deu velha.")
        return table
    elif(first_time == True):
        if(user_moves_first() == True):
            table = user_turn(table)
            table = game_flow(False, 'U', table)
        else:
            table = computer_turn(table)
            table = game_flow(False, 'C', table)
    else:
        if(previous_player == 'C'):
            print("Sua vez.")
            table = user_turn(table)
            table = game_flow(False, 'U', table)
        elif(previous_player == 'U'):
            print("Vez da máquina.")
            table = computer_turn(table)
            table = game_flow(False, 'C', table)
        else:
            print("Ops, algo estranho aconteceu.")
    return table
    
def check_win_conditions(table):
    if(check_rows(table) == True):
        #print(check_rows(table))
        return True
    elif(check_columns(table) == True):
        #print(check_columns(table))
        return True
    elif(check_diagonals(table) == True):
        #print(check_diagonals(table))
        return True
    return False

def print_winner(character):
    if character == 'U':
        print("O usuário venceu!")
    elif character == 'C':
        print("O computador venceu!")
    else:
        print("Não conseguimos detectar o vencedor.")
    return None

def check_rows(table):
    if(table[0][0] == table[0][1] and table[0][1] == table[0][2] 
        and is_empty_string(table[0][0]) == False):
        print_winner(table[0][0])
        return True
    elif(table[1][0] == table[1][1] and table[1][1] == table[1][2] 
        and is_empty_string(table[1][0]) == False):
        print_winner(table[1][0])
        return True
    elif(table[2][0] == table[2][1] and table[2][1] == table[2][2] 
        and is_empty_string(table[2][0]) == False):
        print_winner(table[2][0])
        return True
    else:
        return False

def check_columns(table):
    if(table[0][0] == table[1][0] and table[1][0] == table[2][0] 
        and is_empty_string(table[0][0]) == False):
        print_winner(table[0][0])
        return True
    elif(table[0][1] == table[1][1] and table[1][1] == table[2][1] 
        and is_empty_string(table[0][1]) == False):
        print_winner(table[0][1])
        return True
    elif(table[0][2] == table[1][2] and table[1][2] == table[2][2] 
        and is_empty_string(table[0][2]) == False):
        print_winner(table[0][2])
        return True
    else:
        return False
    
def check_diagonals(table):
    if(table[0][0] == table[1][1] and table[1][1] == table[2][2] 
        and is_empty_string(table[1][1]) == False):
        print_winner(table[0][0])
        return True
    elif(table[0][2] == table[1][1] and table[1][1] == table[2][0] 
        and is_empty_string(table[1][1]) == False):
        print_winner(table[0][2])
        return True
    else:
        return False

def check_if_about_to_win_by_rows(table):
    for i in range(3):
        counter_u = 0
        counter_c = 0
        for j in range(3):
            #empty_column_position = -1
            
            if(is_empty_string(table[i][j]) == False):
                if(table[i][j] == 'U'):
                    counter_u += 1
                elif(table[i][j] == 'C'):
                    counter_c += 1
            elif(is_empty_string(table[i][j]) == True):
                # para armazenar o espaço vazio, caso seja necessário preenchê-lo
                empty_column_position = j
                
        if counter_u == 2 and counter_c == 0:
            # se tiver dois U na linha e nenhum C
            print("Usuário prestes a ganhar.")
            print(i, empty_column_position)
            return i, empty_column_position
        elif counter_c == 2 and counter_u == 0:
            # se tiver dois C na linha e nenhum U
            print("Computador prestes a ganhar.")
            return i, empty_column_position
    return None

def check_if_about_to_win_by_columns(table):
    for j in range(3):
        counter_u = 0
        counter_c = 0
        for i in range(3):
            #empty_row_position = -1
            
            if(is_empty_string(table[i][j]) == False):
                if(table[i][j] == 'U'):
                    counter_u += 1
                elif(table[i][j] == 'C'):
                    counter_c += 1
            elif(is_empty_string(table[i][j]) == True):
                # para armazenar o espaço vazio, caso seja necessário preenchê-lo
                empty_row_position = i
                
        if counter_u == 2 and counter_c == 0:
            # se tiver dois U na linha e nenhum C
            #print("Usuário prestes a ganhar.")
            return empty_row_position, j
        elif counter_c == 2 and counter_u == 0:
            # se tiver dois C na linha e nenhum U
            #print("Computador prestes a ganhar.")
            return empty_row_position, j
    return None

def check_if_about_to_win_by_diagonals(table):
    counter_u = 0
    counter_c = 0
    first_diagonal = [[0,0], [1,1], [2,2]]
    second_diagonal = [[0,2], [1,1], [2,0]]
    #print(first_diagonal[0][0])
    for i in range(len(first_diagonal)):
        pos = first_diagonal[i]
        if(is_empty_string(table[pos[0]][pos[1]]) == False):
            if(table[pos[0]][pos[1]] == 'U'):
                counter_u += 1
            elif(table[pos[0]][pos[1]] == 'C'):
                counter_c += 1
        elif(is_empty_string(table[pos[0]][pos[1]]) == True):
            # para armazenar o espaço vazio, caso seja necessário preenchê-lo
            empty_positions = pos[0], pos[1]    
    if counter_u == 2 and counter_c == 0:
        # se tiver dois U na diagonal e nenhum C
        return empty_positions
    elif counter_c == 2 and counter_u == 0:
        # se tiver dois C na diagonal e nenhum U
        return empty_positions
    
    counter_u = 0
    counter_c = 0
    for i in range(len(second_diagonal)):
        #print(i)
        pos = second_diagonal[i]
        if(is_empty_string(table[pos[0]][pos[1]]) == False):
            if(table[pos[0]][pos[1]] == 'U'):
                counter_u += 1
            elif(table[pos[0]][pos[1]] == 'C'):
                counter_c += 1
        elif(is_empty_string(table[pos[0]][pos[1]]) == True):
            # para armazenar o espaço vazio, caso seja necessário preenchê-lo
            empty_positions = pos[0], pos[1]    
    if counter_u == 2 and counter_c == 0:
        # se tiver dois U na diagonal e nenhum C
        return empty_positions
    elif counter_c == 2 and counter_u == 0:
        # se tiver dois C na diagonal e nenhum U
        return empty_positions
            
    return None

table = create_table_matrix()
print(table)
game_flow(True, None, table)