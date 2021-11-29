# 전반적인 게임로직
import random
from setting import *

class Game():
    def __init__(self, diff):
        self.data = {}
        self.setDiff(diff)

        # 게임창 UI 불러오기

    def setDiff(self,diff): # 난이도에 따른 보물상자 개수 지정
        if diff == "EASY":
            self.goal = 30
            self.remain_key = 45
        elif diff == "NORMAL":
            self.goal = 60
            self.remain_key = 90
        elif diff == "HARD":
            self.goal = 100
            self.remain_key = 150
        self.found_chest = 0

    # 난이도에 따른 보물상자 무작위 배치
    def randomChest(self):
        chests = []

        while len(chests) < 120:
            x = random.randint(0, CELLWIDTH - 1)
            y = random.randint(0, CELLHEIGHT - 1)
            chest = {'x':x, 'y':y}
            if chest not in chests:
                chests.append(chest)

        return chests

    # 게임 데이터
    def gameData(self):
        self.treasure_list = self.randomChest()
        for x in range(0, CELLWIDTH):
            for y in range(0, CELLHEIGHT):
                self.data[(x, y)] = ''

    # 곡괭이 (좌클릭)
    def clickedPickax(self, x, y):
        count = 0
        around_index = []
        if {'x': x, 'y': y} in self.treasure_list and self.data[(x, y)] == '':
            screen.blit(closeTreasure, (50 + 19.4 * x, 95 + 20 * y))
            self.data[(x, y)] = 'closed'
        elif self.data[(x, y)] == '':
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                around_col, around_row = x + i, y + j
                if around_col == -1:
                    around_col = 0
                elif around_col > 30:
                    around_col = 30
                if around_row == -1:
                    around_row = 0
                elif around_row > 19:
                    around_row = 19

                if ({'x': around_col, 'y': around_row} not in around_index) and (around_col != x or around_row != y):
                    around_index.append({'x': around_col, 'y': around_row})

            for index in around_index:
                if index in self.treasure_list:
                    count += 1
            self.showNum(count, x, y)


    def showNum(self, count, x, y):
        if count == 0:
            self.data[(x, y)] = '0'
            screen.blit(zero, (54 + 19.4 * x, 94 + 20 * y))
        elif count == 1:
            self.data[(x, y)] = '1'
            screen.blit(one, (54 + 19.4 * x, 94 + 20 * y))
        elif count == 2:
            self.data[(x, y)] = '2'
            screen.blit(two, (54 + 19.4 * x, 94 + 20 * y))
        elif count == 3:
            self.data[(x, y)] = '3'
            screen.blit(three, (54 + 19.4 * x, 94 + 20 * y))
        elif count == 4:
            self.data[(x, y)] = '4'
            screen.blit(four, (54 + 19.4 * x, 94 + 20 * y))
        elif count == 5:
            self.data[(x, y)] = '5'
            screen.blit(five, (54 + 19.4 * x, 94 + 20 * y))
        elif count == 6:
            self.data[(x, y)] = '6'
            screen.blit(six, (54 + 19.4 * x, 94 + 20 * y))
        elif count == 7:
            self.data[(x, y)] = '7'
            screen.blit(seven, (54 + 19.4 * x, 94 + 20 * y))
        elif count == 8:
            self.data[(x, y)] = '8'
            screen.blit(eight, (54 + 19.4 * x, 94 + 20 * y))


   # 깃발(우클릭)
    def clickedFlag(self, x, y):
        if {'x': x, 'y': y} in self.treasure_list and self.data[(x, y)] == '':
            self.data[(x, y)] = 'flag_treasure'
            screen.blit(redFlag, (53 + 19.4 * x, 92 + 20 * y))
        elif self.data[(x, y)] == 'flag_treasure':
            self.data[(x, y)] = ''
            screen.blit(removeFlag, (53 + 19.4 * x, 92 + 20 * y))
        elif self.data[(x, y)] == '':
            self.data[(x, y)] = 'flag'
            screen.blit(redFlag, (53 + 19.4 * x, 92 + 20 * y))
        elif self.data[(x, y)] == 'flag':
            self.data[(x, y)] = ''
            screen.blit(removeFlag, (53 + 19.4 * x, 92 + 20 * y))

    # 열쇠 (휠클릭)
    def clickedKey(self, x, y):
        if {'x': x, 'y': y} in self.treasure_list and self.data[(x, y)] == '':
            self.data[(x, y)] = "treasure"
            screen.blit(findTreasure, (50 + 19.4 * x, 90 + 20 * y))
            self.goal -= 1
            self.remain_key -= 1
            self.found_chest += 1
        elif self.data[(x, y)] == 'flag_treasure':
            self.data[(x, y)] = "treasure"
            screen.blit(removeFlag, (53 + 19.4 * x, 92 + 20 * y))
            screen.blit(noTreasure, (50 + 19.4 * x, 90 + 20 * y))
            self.remain_key -= 1
        elif self.data[(x, y)] == '':
            self.data[(x, y)] = "empty"
            screen.blit(noTreasure, (50 + 19.4 * x, 90 + 20 * y))
            self.remain_key -= 1
        elif self.data[(x, y)] == 'flag':
            self.data[(x, y)] = "empty"
            screen.blit(removeFlag, (53 + 19.4 * x, 92 + 20 * y))
            screen.blit(noTreasure, (50 + 19.4 * x, 90 + 20 * y))
            self.remain_key -= 1

    # 클릭된 좌표값에 따른 인덱스 값 가져오기
    def cellIndex(self, pos_x, pos_y):
        for x in range(0, 31):
            for y in range(0, 20):
                if 50 + 19.4 * (x + 1) > pos_x > 50 + 19.4 * x and 90 + 20 * (y + 1) > pos_y > 90 + 20 * y:
                    return {'x':x, 'y':y}

    def finished(self):
        if self.goal == 0:
            return True
        else:
            return False
