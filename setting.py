# 변수 정리

import pygame
pygame.init()

# 이미지
guide = pygame.image.load("play_guide.jpg")

# 출처 https://pythonprogramming.altervista.org/buttons-in-pygame/
def button(screen, position, text, size, colors): # ex. colors = "white on blue"
    letter, background = colors.split("on")
    font = pygame.font.SysFont("Algerian", size)
    text_render = font.render(text, 1, letter)
    x, y, w , h = text_render.get_rect()
    x, y = position
    pygame.draw.rect(screen, background, (x, y, w , h))
    return screen.blit(text_render, (x, y))

# 시작 화면

screen_width = 700
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
mbg = pygame.image.load("mbg_a.jpg")
treasure = pygame.image.load("treasure_b.png")

# 게임 화면

background = pygame.image.load("background.jpg")
key_clicked = pygame.image.load("key_clicked.png")
key_notClicked = pygame.image.load("key_notClicked.png")
resetKey = pygame.image.load("resetKey.jpg")
resetStatus = pygame.image.load("resetStatus.png")

findTreasure = pygame.image.load("findTreasure.png")
closeTreasure = pygame.image.load("closeTreasure.png")
noTreasure = pygame.image.load("noTreasure.png")

myTreasure = pygame.image.load("myTreasure.png")
hiddenTreasure = pygame.image.load("hiddenTreasure.png")

redFlag = pygame.image.load("red_flag.jpg")
removeFlag = pygame.image.load("removeFlag.jpg")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (130, 0, 255)
ORANGE = (255, 129, 0)
BROWN = (91, 15, 0)
YELLOW = (171, 160, 0)
BLACK = (0, 0, 0)
PINK = (255, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

n_font = pygame.font.SysFont("Abadi", 20, False, False)
zero = n_font.render("0", True, BLUE)
one = n_font.render("1", True, PURPLE)
two = n_font.render("2", True, ORANGE)
three = n_font.render("3", True, BROWN)
four = n_font.render("4", True, YELLOW)
five = n_font.render("5", True, BLACK)
six = n_font.render("6", True, PINK)
seven = n_font.render("7", True, GREEN)
eight = n_font.render("8", True, RED)

# 결과창
r_font = pygame.font.SysFont("Algerian", 70)
c_font = pygame.font.SysFont("Algerian",40)
successMsg = r_font.render("Success!", True, BLACK)
congMsg = c_font.render("Congratulations", True, BLACK)
failMsg = r_font.render("Fail!", True, BLACK)

CELLWIDTH = 31
CELLHEIGHT = 20