from pygame import*
from time import time as tim
from random import randint

init()
mixer.init() 

window = display.set_mode((1100, 600))
display.set_caption("Fliby Bird")
clock = time.Clock()

background = transform.scale(
    image.load("fliby bird/background.jpg"), (1100, 600))

window.blit(background, (0,0))

mixer.music.load("fliby bird/Angry Birds.mp3") 
mixer.music.play()

class Sprite():
    def __init__(self, filename, x, y, width, height, speed):
        self.speed  = speed
        self.rect = Rect(x, y, width, height)
        self.image = transform.scale(image.load(filename), (70, 70))
    
    def draw_sprite(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def fall(self):
        self.rect.y += self.speed
    
    def up(self):
        self.rect.y -= 40

    def colliderect(self, rect):
        return self.rect.colliderect(rect)
    
class GameCard():

    def __init__(self, x, y, width, height, color = None):
        self.rect = Rect(x, y, width, height)
        self.fill_color = color

    def frame(self, color= (0, 0, 0), thinkness = 5):
        draw.rect(window, color, self.rect, thinkness)

    def draw_rect(self):
        draw.rect(window, self.fill_color, self.rect)
        self.frame()
    
    def colliderect(self, rect):
        return self.rect.colliderect(rect)

    def set_text(self, text, fsize = 70, text_color=(0,0,0)):
        self.image = font.SysFont("Arial", fsize).render(text, True, text_color)

    def draw_text(self, shift_x=5, shift_y=55):
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

    def draw_info(self):
        draw.rect(window, self.fill_color, self.rect)
        window.blit(self.image,(self.rect.x, self.rect.y))

class Wall(Sprite):

    def __init__(self,filename, x, y, width, height):
        self.filename = filename
        self.rect = Rect(x,y,width,height)
        self.image = transform.scale(image.load(filename), (90,400))
    
    def move(self, speed=5):
        self.rect.x -= speed

player = Sprite("fliby bird/player.png",100,250,30,30,1)

walls_down = []
walls_up = []
animation_time = tim()
wall_time = animation_time# інтервал створення монстрів
interval = 5

ready = 3
start = GameCard(0,0,50, 100)

score = 0 
speed = 5
counter = 0 
game = True
while game:
    new_time = tim()

    y = randint(190,300)
    speed += 0.001
    
    for e in event.get():
        if e.type == QUIT:
            mixer.stop()
            mixer.music.load("fliby bird/fail.mp3") 
            mixer.music.play()
            game = False
        
        if e.type == KEYDOWN:
            if e.key ==  K_SPACE:
                player.up() 

        if new_time - wall_time >= interval:
            wall1 = Wall("fliby bird/klipartz.com.png", window.get_width(), (y+100), 30, 240)
            wall2 = Wall("fliby bird/klipartz_up.com.png", window.get_width(), (-y+100), 30, 240)
            walls_down.append(wall1)
            walls_up.append(wall2)
            wall_time = new_time
            interval = randint(1, 5) / 1.5   
        
    player.fall()

    window.blit(background, (0,0))
    player.draw_sprite()

    for wall in walls_down:
        wall.move(speed)
        wall.draw_sprite()
        if player.colliderect(wall):
            window.blit(background, (0,0))
            finish_image = font.SysFont("Goudy Stout", 50).render("YOU LOSE", True, (255,0,0))
            game = False

    for wall in walls_up:
        wall.move(speed)
        wall.draw_sprite()
        if player.colliderect(wall):
            window.blit(background, (0,0))
            finish_image = font.SysFont("Goudy Stout", 50).render("YOU LOSE", True, (255,0,0))
            game = False

    if player.rect.y >= window.get_height() - 60:
        window.blit(background, (0,0))
        finish_image = font.SysFont("Goudy Stout", 50).render("YOU LOSE", True, (255,0,0))
        game = False
    
    if player.rect.y <= 0:
        player.rect.y += 50

    score += speed
    display.update()
    clock.tick(120)
    while counter != 5*60 and game:
        for e in event.get():
            if e.type == QUIT:
                game = False
        counter += 1
        clock.tick(120)

window.blit(finish_image,(window.get_width() / 2 - 220, window.get_height() / 2 - 70))
score = int(score / 100)
mage = font.SysFont("Montserrat", 50).render("SCORE : "+str(score), True, (0,0,0))
window.blit(mage,(window.get_width() / 2 - 100, window.get_height() / 2 + 100))
display.update()
counter = 0
game = True
while counter != 5*60 and game:
        for e in event.get():
            if e.type == QUIT:
                game = False
        counter += 1
        clock.tick(120)