from pygame import*
from random import randint
from menu_dino_pong import*
from main_menu import ending
import sys

init()
clock = time.Clock()

class GameCard():

    def __init__(self, x, y, width, height, text_color, color=None):
        self.rect = Rect(x, y, width, height)
        self.fill_color = color
        self.text_color = text_color

    def new_color(self , color):
        self.fill_color = color

    def frame(self, window, color= (0, 0, 0), thinkness = 5):
        draw.rect(window, color, self.rect, thinkness)

    def draw_rect(self, window):
        draw.rect(window, self.fill_color, self.rect)
        self.frame()

    def set_text(self, text, fsize = 60):
        self.image = font.SysFont("Arial", fsize).render(text, True, self.text_color)

    def draw_text(self, window,  shift_x=5, shift_y=55):
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

    def draw_info(self, window):
        draw.rect(window, self.fill_color, self.rect)
        window.blit(self.image,(self.rect.x, self.rect.y))

class Ball():
    def __init__(self, filename, x, y, width, height, speed_x, speed_y):
        self.rect = Rect(x,y,width,height)
        self.image = transform.scale(image.load(filename), (50, 50))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed_x = speed_x
        self.speed_y = speed_y

    def draw_ball(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Player():
    def __init__(self, filename, x, y, width, height):
        self.rect = Rect(x,y,width,height)
        self.image = transform.scale(image.load(filename), (50, 150))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def draw_player(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
    def move_Up(self):
        self.rect.y -= 7
    
    def move_Down(self):
        self.rect.y += 7

def finish(window, finish_image, gameover, counter = 0):
    window.blit(finish_image,(window.get_width() / 2 - 220, window.get_height() / 2 - 70))
    display.update()
    while counter != 15*60 and not gameover:
        for e in event.get():
            if e.type == QUIT:
                gameover = True
        counter += 1
        clock.tick(120)

choose = Dino_Pong_Menu()

pl1 = 0
pl2 = 0
player1_goals = 0
player2_goals = 0

player1 = Player("Objects_Dino-Pong/player.png", 50, 300, 50, 150)
player2 = Player("Objects_Dino-Pong/player.png", 950, 300, 50, 150)

player1_stats = GameCard(420, 50, 100, 100, (255, 0, 0))

text = GameCard(520, 50, 100, 100, (255, 0, 255))
text.set_text(":")

player2_stats = GameCard(620, 50, 100, 100, (0, 255, 255))

if choose == 1:
    ball_speedx = 3
    ball_speedy = 3

if choose == 2:
    ball_speedx = 4
    ball_speedy = 4

if choose == 3:
    ball_speedx = 5
    ball_speedy = 5


ball = Ball("Objects_Dino-Pong/ball.png", 500, 350, 50, 50, ball_speedx, ball_speedy)

ball_direction_x = randint(1,2)
ball_direction_y = randint(1,2)