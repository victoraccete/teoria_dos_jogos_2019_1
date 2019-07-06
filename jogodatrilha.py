from random import randint

class TablePosition():
    def __init__(self, pos_num, adjs):
        self.pos_num = pos_num
        self.adjs = []
        self.status = 'O'
    
    def set_adjs(self):
        if self.pos_num == 0:
            self.adjs = [1, 2]
        elif self.pos_num == 1:
            self.adjs = [0, 2]
        elif self.pos_num == 2:
            self.adjs = [1, 14]
        elif self.pos_num == 3:
            self.adjs = [4, 10]
        elif self.pos_num == 4:
            self.adjs = [1, 3, 5, 7]
        elif self.pos_num == 5:
            self.adjs = [4, 13]
        elif self.pos_num == 6:
            self.adjs = [7, 11]
        elif self.pos_num == 7:
            self.adjs = [4, 6, 8]
        elif self.pos_num == 8:
            self.adjs = [7, 12]
        elif self.pos_num == 9:
            self.adjs = [0, 10, 21]
        elif self.pos_num == 10:
            self.adjs = [3, 9, 11, 18]
        elif self.pos_num == 11:
            self.adjs = [6, 10, 15]
        elif self.pos_num == 12:
            self.adjs = [8, 13, 17]
        elif self.pos_num == 13:
            self.adjs = [5, 12, 10, 20]
        elif self.pos_num == 14:
            self.adjs = [2, 13, 23]
        elif self.pos_num == 15:
            self.adjs = [11, 16]
        elif self.pos_num == 16:
            self.adjs = [15, 17, 19]
        elif self.pos_num == 17:
            self.adjs = [12, 16]
        elif self.pos_num == 18:
            self.adjs = [10, 19]
        elif self.pos_num == 19:
            self.adjs = [16, 18, 20, 22]
        elif self.pos_num == 20:
            self.adjs = [13, 19]
        elif self.pos_num == 21:
            self.adjs = [9, 22]
        elif self.pos_num == 22:
            self.adjs = [19, 21, 23]
        elif self.pos_num == 23:
            self.adjs = [14, 22] 
          
def user_moves_first():
    if randint(0,1) == 1:
        return True
    else:
        return True # usuario sempre começando 
         
def draw_status_table(positions):
    print("As posições estão enumeradas de 0 a 23, por linha, da esquerda para a direita.")
    print(str(positions[0].status) + " - - - - - " + str(positions[1].status) + 
          " - - - - - " + str(positions[2].status))
    
    print("| - " + str(positions[3].status) + " - - - " + str(positions[4].status) + 
          " - - - " + str(positions[5].status) + " - | ")
    
    print("| - | - " + str(positions[6].status) + " - " + str(positions[7].status) + 
          " - " + str(positions[8].status) + " - | - | ")
    
    print(str(positions[9].status) + " - " + str(positions[10].status) + 
          " - " + str(positions[11].status) + "       " + str(positions[12].status)
          + " - " + str(positions[13].status) + " - " + str(positions[14].status))
    
    print("| - | - " + str(positions[15].status) + " - " + str(positions[16].status) + 
          " - " + str(positions[17].status) + " - | - | ")
    
    print("| - " + str(positions[18].status) + " - - - " + str(positions[19].status) + 
          " - - - " + str(positions[20].status) + " - | ")
    
    print(str(positions[21].status) + " - - - - - " + str(positions[22].status) + 
          " - - - - - " + str(positions[23].status))
    
def mark_table(positions, pos, player):
    if(pos >= 0 and pos <= 24):
        if(positions[pos].status == 'O'):
            positions[pos].status = player
        else:
            print("De 0 a 23.")
            positions = mark_table(positions, pos, player)
    return positions

def choose_first_pos(positions):
    for i in range(24):
        if(positions[i].status == 'O'):
            return mark_table(positions, i, 'C')
    return positions

def pieces_positioning(positions):
    user_counter = 0
    ai_counter = 0
    if(user_moves_first() == True):
        pos = int(input("Escolha a posição de 0 a 23:\n"))
        positions = mark_table(positions, pos, 'U')
        positions = choose_first_pos(positions)
        user_counter += 1
        ai_counter += 1
        draw_status_table(positions)
        while(user_counter < 9 and ai_counter < 9):
            pos = int(input("Escolha a posição de 0 a 23:\n"))
            positions = mark_table(positions, pos, 'U')
            positions = choose_first_pos(positions)
            user_counter += 1
            ai_counter += 1
            draw_status_table(positions)
    else:
        positions = choose_first_pos(positions)
        draw_status_table(positions)
        pos = int(input("Escolha a posição de 0 a 23:\n"))
        positions = mark_table(positions, pos, 'U')
        ai_counter += 1
        user_counter += 1 
        draw_status_table(positions)
        while(user_counter < 9 and ai_counter < 9):
            positions = choose_first_pos(positions)
            draw_status_table(positions)
            pos = int(input("Escolha a posição de 0 a 23:\n"))
            positions = mark_table(positions, pos, 'U')
            ai_counter += 1
            user_counter += 1 
            draw_status_table(positions)
    return positions

positions = []
for i in range(24):
    pos = TablePosition(i, [])
    pos.set_adjs()
    positions.append(pos)

# Esse 'for' é desnecessário:   
#for i in range(24):
#    print(positions[i].pos_num)
#    print(positions[i].adjs)
    

draw_status_table(positions)
pieces_positioning(positions)
#positions = mark_table(positions, 23, 'C')
#positions = mark_table(positions, 12, 'U')
#draw_status_table(positions)