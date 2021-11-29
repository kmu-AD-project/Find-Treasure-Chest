import pygame
import sys
from setting import *
from game_function import Game


# 게임 첫 시작화면
# 보물 상자 개수 선택/게임방법 설명 버튼

class StartScreen():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Where\'s my treasure chest')
        screen.fill(WHITE)
        t_font = pygame.font.SysFont("Algerian", 42, False, False)
        title = t_font.render("Where\'s my treasure chest", True, BLACK)
        screen.blit(mbg, (580, 0))
        screen.blit(treasure, (50, 250))
        screen.blit(title, (50, 100))

        self.easy = button(screen, (490, 230), "EASY", 35, "black on white")
        self.normal = button(screen, (490, 300), "NORMAL", 35, "black on white")
        self.hard = button(screen, (490, 370), "HARD", 35, "black on white")
        self.play_guide = button(screen, (490, 440), "Play Guide", 35, "black on white")

        pygame.display.update()

    def running(self):
        running = True
        closeGuide = None
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.easy.collidepoint(pygame.mouse.get_pos()):
                        pygame.display.set_caption("EASY")
                        return "EASY"
                    elif self.normal.collidepoint(pygame.mouse.get_pos()):
                        pygame.display.set_caption("NORMAL")
                        return "NORMAL"
                    elif self.hard.collidepoint(pygame.mouse.get_pos()):
                        pygame.display.set_caption("HARD")
                        return "HARD"

                    if self.play_guide.collidepoint(pygame.mouse.get_pos()):
                        pygame.display.set_caption("Play Guide")
                        screen.blit(guide, (0, 0))
                        closeGuide = button(screen, (530, 50), " Return to MAIN ", 20, "red on white")
                        pygame.display.update()

                    if closeGuide and closeGuide.collidepoint(pygame.mouse.get_pos()):
                        main.main()


class GameScreen():
    def __init__(self, difficulty):
        self.gameLogic = Game(difficulty)

        # 배경 배치
        screen.fill(WHITE)
        screen.blit(background, (50, 90))
        # 버튼 배치
        self.showStatus()
        screen.blit(key_notClicked, (62, 62))
        screen.blit(myTreasure, (180, 60))
        screen.blit(hiddenTreasure, (260, 60))
        self.exitGame = button(screen, (600, 60), " EXIT ", 15, "white on black")

        pygame.display.update()
        
        self.gameLogic.gameData()

    def showStatus(self):
        if self.gameLogic.remain_key == 9 or self.gameLogic.goal == 9:
            screen.blit(resetStatus, (100, 60))
            screen.blit(myTreasure, (180, 60))
            screen.blit(hiddenTreasure, (260, 60))
            self.exitGame = button(screen, (600, 60), " EXIT ", 15, "white on black")
        self.keyStatus = button(screen, (100, 60), "{}".format(self.gameLogic.remain_key), 20, "black on white")
        self.findStatus = button(screen, (220, 60), "{}".format(self.gameLogic.found_chest), 20, "black on white")
        self.leftStatus = button(screen, (300, 60), "{}".format(self.gameLogic.goal), 20, "black on white")

    def running(self):
        running = True

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    # 종료 버튼
                    if self.exitGame.collidepoint(pygame.mouse.get_pos()):
                        main.main()

                    try:
                        index = self.gameLogic.cellIndex(event.pos[0], event.pos[1])
                        x = index['x']
                        y = index['y']

                        # 열쇠 아이콘 기본 세팅
                        screen.blit(resetKey, (60, 60))
                        screen.blit(key_notClicked, (62, 62))

                        # 곡괭이 (좌클릭)
                        if event.button == 1:
                            self.gameLogic.clickedPickax(x, y)
                            pygame.display.update()

                        # 열쇠 (휠클릭)
                        elif event.button == 2:
                            screen.blit(resetKey, (60, 60))
                            screen.blit(key_clicked, (60, 60))
                            self.gameLogic.clickedKey(x, y)
                            self.showStatus()
                            pygame.display.update()

                        # 깃발 (우클릭)
                        elif event.button == 3:
                            self.gameLogic.clickedFlag(x, y)
                            pygame.display.update()

                    except TypeError:
                        pass

            # 게임 결과 
            foundChest = self.gameLogic.found_chest
            leftChest = self.gameLogic.goal

            if self.gameLogic.finished():
                return foundChest, leftChest, True

            elif self.gameLogic.remain_key == 0:
                return foundChest, leftChest, False

class ResultScreen():
        def __init__(self, gameResult):
            count, remain, ifSuccess = gameResult

            screen.fill(WHITE)
            self.goToMain = button(screen, (490, 370), " MAIN ", 50, "white on black")
            c_font = pygame.font.SysFont("Algerian", 30)
            countMsg = c_font.render("You found " + str(count) + " Treasure Chest", True, BLACK)
            remainMsg = c_font.render("Until the goal " + str(remain), True, BLACK)

            if ifSuccess:
                screen.blit(successMsg, (100, 100))
                screen.blit(congMsg, (100, 200))
                screen.blit(countMsg, (100, 300))

            else:
                screen.blit(failMsg, (100, 100))
                screen.blit(countMsg, (100, 200))
                screen.blit(remainMsg, (100, 300))

            pygame.display.update()

        def running(self):
            running = True

            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse = pygame.mouse.get_pos()
                        if self.goToMain.collidepoint(mouse):
                            main.main()

class Main():
    def main(self):
        startScreen = StartScreen()
        difficulty = startScreen.running()
        gameScreen = GameScreen(difficulty)
        gameResult = gameScreen.running()
        resultScreen = ResultScreen(gameResult)
        resultScreen.running()


if __name__ == '__main__':
    while True:
        main = Main()
        main.main()