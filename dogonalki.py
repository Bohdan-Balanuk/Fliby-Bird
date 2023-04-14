def Dogonalki_game():
    import pygame 

    pygame.init()

    # створення вікна
    window = pygame.display.set_mode((1100,600))
    pygame.display.set_caption("Догонялки")

    clock = pygame.time.Clock()

    background = pygame.transform.scale(
        pygame.image.load("dogonalky/background.jpg"), # image.load - завантажує картинку
        (1100, 600)) # масштабувати до розмірів 1200х1080

    window.blit(background, (0,0)) # у вікні window намалювати зображення в координатах 0,0

    class Sprite:

        def __init__(self, filename, x, y, width, height, speed):
            self.speed = speed
            self.rect = pygame.Rect(x, y, width, height)
            self.image = pygame.transform.scale(pygame.image.load(filename), (100, 100))

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

    player1 = Sprite("dogonalky/sprite1.png", 100, 250, 50, 50, 10)
    player2 = Sprite("dogonalky/sprite2.png", 900, 250, 50, 50, 10)

    game = True
    while game:
        # event.get() - список всіх подій
        # якщо користувач натиснув на крестик закрити
        for e in pygame.event.get(): # для кожної події
            if e.type == pygame.QUIT: # якщо тип події - натиснути на хрестик
                game = False

        pressed_keys = pygame.key.get_pressed()# повертає нам клавіши, які ми натиснули
        if pressed_keys[pygame.K_w]:
            player1.move_up()
        if pressed_keys[pygame.K_s]:
            player1.move_down()
        if pressed_keys[pygame.K_a]:
            player1.move_left()
        if pressed_keys[pygame.K_d]:
            player1.move_right()

        if pressed_keys[pygame.K_UP]:
            player2.move_up()
        if pressed_keys[pygame.K_DOWN]:
            player2.move_down()
        if pressed_keys[pygame.K_LEFT]:
            player2.move_left()
        if pressed_keys[pygame.K_RIGHT]:
            player2.move_right()

        if player1.colliderect(player2):
            game = False
            finish_image = pygame.font.SysFont("Goudy Stout",50).render("GAMEOVER", True, (178, 34, 34))

        window.blit(background, (0,0))
        player1.draw_sprite()
        player2.draw_sprite()

        pygame.display.update()
        clock.tick(60)

    counter = 0 
    window.blit(finish_image, (300,200))  
    pygame.display.update()
    game = True
    while counter != 5*45 and game:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game = False
        counter += 1
        clock.tick(120)
