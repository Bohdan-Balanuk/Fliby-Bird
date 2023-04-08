from pygame import*
from map_labirint import*
from random import randint

init()
mixer.init() # music on

window = display.set_mode((1100, 600))
display.set_caption("Лабіринт")
clock = time.Clock()

background = transform.scale(
    image.load("labirint/background.png"), (1100, 600))

window.blit(background, (0,0))

mixer.music.load("labirint/Топ музон.mp3") 
mixer.music.play()

kick = mixer.Sound("labirint/kick.ogg")
take_money = mixer.Sound("labirint/money.ogg")



class Sprite():
    def __init__(self, filename, x, y, width, height, speed):
        self.speed = speed
        self.rect = Rect(x, y, width, height)
        self.image = transform.scale(image.load(filename), (40, 40))
    
    def draw_sprite(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
    def move_up(self):
        if self.rect.y >=0:
            self.rect.y -= self.speed
    def move_down(self):
        if self.rect.y + self.rect.height <= window.get_height():
            self.rect.y += self.speed
    def move_left(self):
        if self.rect.x >=0:
            self.rect.x -= self.speed
    def move_right(self):
        if self.rect.x + self.rect.width <= window.get_width():
            self.rect.x += self.speed

    def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Enemy(Sprite):
    def update(self, coord1, coord2):
        # якщо спрайт досягнув 1 точки - змінити маршрут в сторону другої
        # рух по горизонталі
        if self.rect.x <= coord1 or self.rect.x >= coord2:
            self.speed *= -1
        self.rect.x += self.speed
        
    def update_hor(self, coord1, coord2):
        if self.rect.y <= coord1 or self.rect.y >= coord2:
            self.speed *= -1
        self.rect.y += self.speed
    
    def random_update(self):
        global direction
        old_speed = self.speed
        old_direction = direction
        if self.rect.y <= 0:
            if direction == 1:
                    self.speed *= -1
                    self.rect.x += self.speed
                    self.speed *= -1
            if direction == 2:
                    self.speed *= -1
                    self.rect.y += self.speed
                    self.speed *= -1
            while old_direction == direction and old_speed == self.speed:
                    direction = randint(1, 2)
                    self.speed = randint(-1, 1)
            while self.speed == 0:
                    self.speed = randint(-1, 1)

        if self.rect.y + self.rect.height >= window.get_height():
            if direction == 1:
                    self.speed *= -1
                    self.rect.x += self.speed
                    self.speed *= -1
            if direction == 2:
                    self.speed *= -1
                    self.rect.y += self.speed
                    self.speed *= -1               
            while old_direction == direction and old_speed == self.speed:
                    direction = randint(1, 2)
                    self.speed = randint(-1, 1)
            while self.speed == 0:
                    self.speed = randint(-1, 1)

        if self.rect.x <=0:
            if direction == 1:
                    self.speed *= -1
                    self.rect.x += self.speed
                    self.speed *= -1
            if direction == 2:
                    self.speed *= -1
                    self.rect.y += self.speed
                    self.speed *= -1
            while old_direction == direction and old_speed == self.speed:
                    direction = randint(1, 2)
                    self.speed = randint(-1, 1)
            while self.speed == 0:
                    self.speed = randint(-1, 1)

        if self.rect.x + self.rect.width >= window.get_width():
            if direction == 1:
                    self.speed *= -1
                    self.rect.x += self.speed
                    self.speed *= -1
            if direction == 2:
                    self.speed *= -1
                    self.rect.y += self.speed
                    self.speed *= -1
            while old_direction == direction and old_speed == self.speed:
                    direction = randint(1, 2)
                    self.speed = randint(-1, 1)
            while self.speed == 0:
                    self.speed = randint(-1, 1)

        for wall in game_map:
            if self.colliderect(wall):
                # крок назад
                if direction == 1:
                    self.speed *= -1
                    self.rect.x += self.speed
                    self.speed *= -1
                if direction == 2:
                    self.speed *= -1
                    self.rect.y += self.speed
                    self.speed *= -1
                # рандом напрямок 1-х 2-у
                while old_direction == direction and old_speed == self.speed:
                    direction = randint(1, 2)
                    self.speed = randint(-1, 1)
                while self.speed == 0:
                    self.speed = randint(-1, 1)

        if direction == 1:
            self.rect.x += self.speed
        if direction == 2:
            self.rect.y += self.speed


    #Коли гравець доторкнувся до стіни - рандомно обрати сторону (х, у). 
    #Потім обрати швидкість (додатню, від'ємну) (якщо швидкість і напрямок такі ж як зараз, то повторити)
        

player = Sprite("labirint/player.png", 100, 80, 30, 30, 1)
enemy1 = Enemy("labirint/enemy.png", 900, 250, 30, 30, 1)
enemy2 = Enemy("labirint/enemy.png", 480, 510, 30, 30, 1)
enemy3 = Enemy("labirint/enemy.png", 780, 510, 30, 30, 1)
enemy4 = Enemy("labirint/enemy.png", 5, 80, 30, 30, 1)
money = Sprite("labirint/treasure.png", 1000, 500, 55, 55, 0)
direction = 1
counter = 0 
game = True



game_map = make_map()

while game:

    for e in event.get(): 
        if e.type == QUIT: 
            game = False

    window.blit(background, (0,0))
    for wall in game_map:
        wall.draw_rect(window)

    player.draw_sprite()
    enemy1.draw_sprite()
    enemy2.draw_sprite()
    enemy3.draw_sprite()
    enemy4.draw_sprite()
    money.draw_sprite()

    enemy1.update(870,1030)
    enemy2.update_hor(50,510)
    enemy3.update_hor(50,510)
    enemy4.random_update()      

    pressed_keys = key.get_pressed()
    if pressed_keys[K_UP]:
        player.move_up()
    if pressed_keys[K_DOWN]:
        player.move_down()
    if pressed_keys[K_LEFT]:
        player.move_left()
    if pressed_keys[K_RIGHT]:
        player.move_right()

    for wall in game_map:
        if player.colliderect(wall):
            player.rect.x = 50
            player.rect.y = 10

    if player.colliderect(money):
        take_money.play()
        game = False
        finish_image = font.SysFont("Goudy Stout",50).render("You won", True, (173, 255, 47))

    if player.colliderect(enemy1) or player.colliderect(enemy2) or player.colliderect(enemy3) or player.colliderect(enemy4):
        kick.play()
        game = False
        mixer.music.load("labirint/fail.mp3") 
        mixer.music.play()
        finish_image = font.SysFont("Goudy Stout",50).render("You lose", True, (178, 34, 34))

    display.update()
    clock.tick(120)
    while counter != 5*60 and game:
        for e in event.get():
            if e.type == QUIT:
                game = False
        counter += 1
        clock.tick(120)
        
counter = 0 
window.blit(finish_image, (450,200))  
display.update()
game = True
while counter != 5*60 and game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    counter += 1
    clock.tick(120)
