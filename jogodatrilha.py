# -*- coding: utf-8 -*-

class TablePosition():
    def __init__(self, pos_num, adjs):
        self.pos_num = pos_num
        self.adjs = []
    
    def set_adjs(self):
        if self.pos_num == 1:
            self.adjs = [2, 3]
        elif self.pos_num == 2:
            self.adjs = [1, 3]
        elif self.pos_num == 3:
            self.adjs = [2, 15]
        elif self.pos_num == 4:
            self.adjs = [5, 11]
        elif self.pos_num == 5:
            self.adjs = [2, 4, 6, 8]
        elif self.pos_num == 6:
            self.adjs = [5, 14]
        elif self.pos_num == 7:
            self.adjs = [8, 12]
        elif self.pos_num == 8:
            self.adjs = [5, 7, 9]
        elif self.pos_num == 9:
            self.adjs = [8, 13]
        elif self.pos_num == 10:
            self.adjs = [1, 11, 22]
        elif self.pos_num == 11:
            self.adjs = [4, 10, 12, 19]
        elif self.pos_num == 12:
            self.adjs = [7, 11, 16]
        elif self.pos_num == 13:
            self.adjs = [9, 14, 18]
        elif self.pos_num == 14:
            self.adjs = [6, 13, 11, 21]
        elif self.pos_num == 15:
            self.adjs = [3, 14, 24]
        elif self.pos_num == 16:
            self.adjs = [12, 17]
        elif self.pos_num == 17:
            self.adjs = [16, 18, 20]
        elif self.pos_num == 18:
            self.adjs = [13, 17]
        elif self.pos_num == 19:
            self.adjs = [11, 20]
        elif self.pos_num == 20:
            self.adjs = [17, 19, 21, 23]
        elif self.pos_num == 21:
            self.adjs = [14, 20]
        elif self.pos_num == 22:
            self.adjs = [10, 23]
        elif self.pos_num == 23:
            self.adjs = [20, 22, 24]
        elif self.pos_num == 24:
            self.adjs = [15, 23]            

positions = []
for i in range(24):
    pos = TablePosition(i, [])
    pos.set_adjs()
    positions.append(pos)
    
for i in range(24):
    print(positions[i].pos_num)
    print(positions[i].adjs)
    
#print(positions[20].adjs)