### This code  draws 'Random Non Overlapping Circles'.###
### Sahil Islam ###
### Date: 28/05/2020 ###

import pygame
import numpy as np
import random

pygame.init()
display_width = 800
display_height = 500

black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
whiten = [230, 230, 250]

display_surface = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
pygame.display.set_caption("Random Circle")


def circle(x, y, r): #Defining a function that draws a circle with centre at (x,y) and radius r.
    pygame.draw.circle(display_surface, red, (int(x), int(y)), int(r), 2)


def distance(x1, y1, x2, y2):  #Defining a function that calculates distance between two points (x1,y1) and (x2,y2).
    dsq = (x1 - x2) ** 2 + (y1 - y2) ** 2
    d = np.sqrt(dsq)
    return d


display_surface.fill(black)
n = 250  #This is the number o circles.

circleList = []
while (len(circleList) < n):    #Thi while loop runs untill it reaches the desired circle number.

    r = random.randint(10, 20)
    x = random.randint(r, display_width - r)
    y = random.randint(r, display_height - r)

    overlap = False
    for x2, y2, r2 in circleList:
        d = distance(x, y, x2, y2)
        if d < r + r2:      #Overlapping condition.
            overlap = True
            break

    if not overlap:
        circleList.append((x, y, r))

        circle(x, y, r)

    pygame.display.update()
    clock.tick(200)

exit = False
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
