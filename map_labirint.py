import pygame
# 1 Square = 1/12 нашої висоти
# A - Wall
# B - Space
map = [
    ["-","A","A","A","A","A","A","A","A","A","A","A","A"],
    ["_","-","A","-","-","-","-","A","-","A","A","-","_"],
    ["_","-","A","-","A","-","-","-","-","A","A","-","_"],
    ["A","-","A","-","A","-","A","-","A","A","-","-","A"],
    ["A","-","A","-","A","-","A","-","-","A","A","-","A"],
    ["A","-","A","-","A","-","A","-","-","A","-","-","A"],
    ["A","-","A","-","-","-","A","A","-","A","A","-","A"],
    ["A","-","A","-","A","-","A","A","-","A","-","-","A"],
    ["A","-","A","-","A","-","A","-","-","A","A","-","A"],
    ["A","-","A","-","A","-","A","-","A","A","-","-","A"],
    ["A","-","-","-","A","-","A","-","-","-","-","-","A"],
    ["A","A","A","A","A","A","A","A","A","A","A","A","A"]
]

SIZE = 600 / 12
# Клас стіна
class Wall:

    def __init__(self, x, y, width=SIZE, height=SIZE, color=(30, 144, 255)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
    def draw_rect(self, window):
        pygame.draw.rect(window, self.color, self.rect)

def make_map(): # Алгоритм, який перетворю текст в стіну
    walls = [] # список у якому зберігаються стіни
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "A":
                wall_x = (x + 4.5)* SIZE
                wall_y = y * SIZE
                wall = Wall(wall_x, wall_y)
                walls.append(wall)
    return walls