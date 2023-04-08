import pygame
import time   
import random
pygame.init()
window = pygame.display.set_mode( (1000, 500) )
pygame.display.set_caption("Дінозавр")
BACKGROUND = (254, 220, 224)
window.fill(BACKGROUND)
clock = pygame.time.Clock()

class Dino:

    def __init__ (self, filename, x, y, width=35, height=35):
        self.hitbox = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(filename[0])#додаємо як картинку перший елемент списку
        self.animation_list = filename#зберігаємо список
        self.animation = 0#запам'ятовуємо індекс картинки, яка на екрані зараз
    def draw_sprite(self):
        window.blit(self.image, (self.hitbox.x, self.hitbox.y))
    def next_image(self):
        if self.animation == 0:
            self.image = pygame.image.load(self.animation_list[1])
            self.animation = 1
        else:
            self.image = pygame.image.load(self.animation_list[0])
            self.animation = 0
    def is_collide(self, enemy):
        return self.hitbox.colliderect(enemy.hitbox)

class Enemy(Dino):
    
    def move_enemy(self, speed=5):
        self.hitbox.x -= speed

animation_list = ["dino/dino1.png", "dino/dino2.png"] #"dino1.png", "dino2.png"
dino = Dino(animation_list, 50, 250, 50, 50)
rock = ["dino/small_rock.png"]
#створюємо монстрів
enemies = []
animation_time = time.time()
enemy_time = animation_time# інтервал створення монстрів
platform = pygame.Rect(0, 300, window.get_width(), 200)
jump = False
counter = 0
interval = 5
gameover = False
score = 0
speed = 5
while not gameover:
    new_time = time.time()
    #перемикання анімації
    if new_time - animation_time >= 0.1:
        dino.next_image()
        animation_time = new_time
    #створення перешкод
    if new_time - enemy_time >= interval:
        enemy = Enemy(rock, window.get_width(), 270, 30, 30)#(список з анімацій, ширина вікна, 270, 30, 30)
        enemies.append(enemy)
        enemy_time = new_time
        interval = random.randint(1, 5) / 1.5


    #збыльшення швидкості
    speed += 0.001
    window.fill(BACKGROUND)
    pygame.draw.rect(window, (207, 209, 253), platform)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump = True
    #алгоритм стрибка
    if jump == True:
        if counter < 15:
            dino.hitbox.y -= 7
            counter += 1
        elif 14 < counter < 30:
            dino.hitbox.y += 7
            counter += 1
        else:
            counter = 0
            jump = False
            
    for enemy in enemies:
        enemy.move_enemy(speed)
        enemy.draw_sprite()
        if dino.is_collide(enemy):
            gameover = True
        if enemy.hitbox.x + enemy.hitbox.width <= 0:
            enemies.remove(enemy)

    dino.draw_sprite()
    score += int(speed)
    pygame.display.update()
    clock.tick(60)

image = pygame.font.SysFont("Montserrat", 50).render("GAME OVER", True, (0,0,0))
window.blit(image,(window.get_width() / 2 - 100, window.get_height() / 2 - 100))
score = int(score / 100)
mage = pygame.font.SysFont("Montserrat", 50).render("SCORE : "+str(score), True, (0,0,0))
window.blit(mage,(window.get_width() / 2 - 100, window.get_height() / 2 + 100))
pygame.display.update()
time.sleep(5)