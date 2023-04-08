from pygame import*
from time import time as time1
from random import randint 
from classes_objects_and_menu_dino_pong import* 
import sys

init()
clock = time.Clock()

window = display.set_mode((1050, 750))
display.set_caption('Dino-Pong')
background = transform.scale(image.load("Objects_Dino-Pong/Поле.jpg"), (1050, 750))
window.blit(background, (0,0))

gameover = False

while not gameover:
    counter = 0

    for ev in event.get():
        if ev.type == QUIT:
            gameover = True
        
        if ev.type == KEYDOWN:
            if ev.key == K_w:
                pl1 = 1
            if ev.key == K_s:
                pl1 = -1

            if ev.key == K_UP:
                pl2 = 1
            if ev.key == K_DOWN:
                pl2 = -1
        
        if ev.type == KEYUP:
            if ev.key == K_w:
                pl1 = 0
            if ev.key == K_s:
                pl1 = 0
            
            if ev.key == K_UP:
                pl2 = 0
            if ev.key == K_DOWN:
                pl2 = 0

    # движение гравців
    if pl1 == 1 and player1.rect.y >= 0:
        player1.move_Up() 
    if pl1 == -1 and player1.rect.y <= 600:
        player1.move_Down() 

    if pl2 == 1 and player2.rect.y >= 0:
        player2.move_Up() 
    if pl2 == -1 and player2.rect.y <= 600:
        player2.move_Down() 

    # рандом напрямок(лише спочатку гри)
    if ball_direction_x == 1:
        ball.rect.x -= ball.speed_x
    if ball_direction_x == 2:
        ball.rect.x += ball.speed_x

    if ball_direction_y == 1:
        ball.rect.y += ball.speed_y
    if ball_direction_y == 2:
        ball.rect.y -= ball.speed_y

    # відскакування мяча від полу й потолку
    if ball.rect.y >= 700:
        ball.speed_y *= -1

        if choose == 1:
            if ball.speed_y < 0:
                ball.speed_y -= 0.2
            else:
                ball.speed_y += 0.2

        if choose == 2:
            if ball.speed_y < 0:
                ball.speed_y -= 0.3
            else:
                ball.speed_y += 0.3

        if choose == 3:
            if ball.speed_y < 0:
                ball.speed_y -= 0.35
            else:
                ball.speed_y += 0.35     
        
    if ball.rect.y <= 0:
        ball.speed_y *= -1

        if choose == 1:
            if ball.speed_y < 0:
                ball.speed_y -= 0.2
            if ball.speed_y > 0:
                ball.speed_y += 0.2

        if choose == 2:
            if ball.speed_y < 0:
                ball.speed_y -= 0.3
            if ball.speed_y > 0:
                ball.speed_y += 0.3

        if choose == 3:
            if ball.speed_y < 0:
                ball.speed_y -= 0.35
            if ball.speed_y > 0:
                ball.speed_y += 0.35

    #кінець
    if choose == 1:
        if player1_goals == 4:
            finish_image = font.SysFont("Goudy Stout", 25).render("Left player WIN", True, (255, 0, 255))
            finish(window, finish_image, gameover)
            gameover = True

        if player2_goals == 4: 
            finish_image = font.SysFont("Goudy Stout", 25).render("Right player WIN", True, (255, 0, 255))
            finish(window, finish_image, gameover)
            gameover = True
        
    if choose == 2:
        if player1_goals == 6:
            finish_image = font.SysFont("Goudy Stout", 25).render("Left player WIN", True, (255, 0, 255))
            finish(window, finish_image, gameover)
            gameover = True

        if player2_goals == 6: 
            finish_image = font.SysFont("Goudy Stout", 25).render("Right player WIN", True, (255, 0, 255))
            finish(window, finish_image, gameover)
            gameover = True
    
    if choose == 3:
        if player1_goals == 8:
            finish_image = font.SysFont("Goudy Stout", 25).render("Left player WIN", True, (255, 0, 255))
            finish(window, finish_image, gameover)
            gameover = True

        if player2_goals == 8: 
            finish_image = font.SysFont("Goudy Stout", 25).render("Right player WIN", True, (255, 0, 255))
            finish(window, finish_image, gameover)
            gameover = True

    # реагування мяча на гравців    
    if ball.colliderect(player1):
        ball.speed_x *= -1
    if ball.colliderect(player2):
        ball.speed_x *= -1

    # реакція мяча за виліт карти
    if ball.rect.x >= 1100 or ball.rect.x <= -100:
        if ball.rect.x >= 1100:
            player1_goals += 1
        if ball.rect.x <= -100:
            player2_goals += 1
        ball.rect.x = 500
        ball.rect.y = 350
        ball.speed_y = ball_speedy

    window.blit(background, (0,0))
    player1.draw_player(window)
    player2.draw_player(window)   
    ball.draw_ball(window)

    player1_stats.set_text(str(player1_goals))
    player2_stats.set_text(str(player2_goals))

    player1_stats.draw_text(window)    
    player2_stats.draw_text(window)    
    text.draw_text(window)

    display.update()
    clock.tick(120)