#coding=utf-8

import sys
import random

class PlayGobang():

    def __init__(self):
        self.checkerboard = None
        self.round = 10
        self.dim = 10
        self.max_len = 2

    def init_checkerboard(self):
        #初始化棋盘
        self.checkerboard = []
        for i in range(self.dim):
            row = ['.' for x in range(self.dim)]
            self.checkerboard.append(row)

    def display_checkerboard(self):
        #打印当前棋盘
        dim = len(self.checkerboard)
        for i in range(dim):
            print('    '.join(self.checkerboard[i]))
            print('')
        print('')
    
    def is_game_end(self):
        #检查是否决出胜负
        for i in range(self.dim):
            for j in range(self.dim):
                cur_state = self.checkerboard[i][j]
                if cur_state == '.':
                    continue
                continue_num = 0
                #检查行
                is_row_end = True
                for k in range(self.max_len):
                    if (j+k) >= self.dim or self.checkerboard[i][j+k] != cur_state:
                        is_row_end = False
                        break
                    else:
                        continue_num += 1
                if continue_num >= self.max_len:
                    return True
                #检查列
                continue_num = 0
                is_colum_end = True
                for k in range(self.max_len):
                    if (i+k) >= self.dim or self.checkerboard[i+k][j] != cur_state:
                        is_colum_end = False
                        break
                    else:
                        continue_num += 1
                if continue_num >= self.max_len:
                    return True
                #检查左上到右下
                continue_num  = 0
                is_upper_left_end = True
                for k in range(self.max_len):
                    if (i+k) >= self.dim or (j+k) >= self.dim or self.checkerboard[i+k][j+k] != cur_state:
                        is_upper_left_end = False
                        break
                    else:
                        continue_num += 1
                if continue_num >= self.max_len:
                    return True
                #检查右上到左下
                is_upper_right_end = True
                continue_num = 0
                for k in range(self.max_len):
                    if (i+k) >= self.dim or (j-k) < 0:
                        is_upper_right_end = False
                        break
                    elif self.checkerboard[i+k][j-k] != cur_state:
                        is_upper_right_end = False
                        break
                    else :
                        continue_num += 1
                if continue_num >= self.max_len:
                    return True
        return False
    
    def random_move_once(self, t):
        color = 'x'
        if t == 1:
            color = 'o'
        else:
            color = 'x'
        while True:
            i = random.randint(0, self.dim-1)
            j = random.randint(0, self.dim-1)
            if self.checkerboard[i][j] == '.':
                self.checkerboard[i][j] = color
                break

    
    def run(self):
        #运行游戏
        self.init_checkerboard()
        color = True
        for i in range(self.round):
            self.random_move_once(color)
            color = ~color
            print("Round:%d"%(i+1))
            self.display_checkerboard()
            if self.is_game_end():
                print("Game Over")
                break
            self.random_move_once(color)
            self.display_checkerboard()
            if self.is_game_end():
                print("Game Over")
                break

    
    # def begin_game(self, )


game = PlayGobang()
game.run()