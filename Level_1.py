#!/usr/bin/env python3

import pygame, sys
from pygame.locals import *

pygame.init()
#DISPLAY = (600, 450)
XVALUE = 1024
YVALUE = int(XVALUE * 1536/2048)
DISPLAY = (XVALUE, YVALUE)

windowSurface = pygame.display.set_mode(DISPLAY, 0, 32)
pygame.display.set_caption('SHORT -N- SWEET')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
BLUEGREEN = (0, 128, 128)
YELLOW = (255, 255, 0)



windowSurface.fill(BLACK)

#pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
#pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
#pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120))
#pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)

#CIRCLES
FIRSTCIRCLE = (0.85, 0.18)
POSCIRCLES = (\
    (FIRSTCIRCLE[0] * DISPLAY[0], FIRSTCIRCLE[1] * DISPLAY[1]), \
    ((FIRSTCIRCLE[0] + 0.05) * DISPLAY[0], (FIRSTCIRCLE[1] + 0.05) * DISPLAY[1]), \
    ((FIRSTCIRCLE[0] + 0.05) * DISPLAY[0], (FIRSTCIRCLE[1] + 0.13) * DISPLAY[1]), \
    ((FIRSTCIRCLE[0] - 0.69) * DISPLAY[0], (FIRSTCIRCLE[1] + 0.36) * DISPLAY[1]), \
    ((FIRSTCIRCLE[0] - 0.69) * DISPLAY[0], (FIRSTCIRCLE[1] + 0.51) * DISPLAY[1]), \
    ((FIRSTCIRCLE[0] - 0.75) * DISPLAY[0], (FIRSTCIRCLE[1] + 0.46) * DISPLAY[1]), \
    ((FIRSTCIRCLE[0] - 0.75) * DISPLAY[0], (FIRSTCIRCLE[1] + 0.61) * DISPLAY[1]), \
    ((FIRSTCIRCLE[0] - 0.63) * DISPLAY[0], (FIRSTCIRCLE[1] + 0.46) * DISPLAY[1]), \
    ((FIRSTCIRCLE[0] - 0.63) * DISPLAY[0], (FIRSTCIRCLE[1] + 0.57) * DISPLAY[1]), \
    ((FIRSTCIRCLE[0] - 0.60) * DISPLAY[0], (FIRSTCIRCLE[1] + 0.64) * DISPLAY[1]))
CIRCLESIZE = (8*(DISPLAY[0]/600))
NUMBERCIRCLES = len(POSCIRCLES)
for i in range (0, NUMBERCIRCLES):
    pygame.draw.circle(windowSurface, PURPLE, (POSCIRCLES[i]), CIRCLESIZE, 0)


#RECTANGULARS

RECTSIZE = (15*(DISPLAY[0]/600))

#bottom line
for i in range (0, 20):
    pygame.draw.rect(windowSurface, WHITE, (0 + (i * 2 * RECTSIZE), (DISPLAY[1] - (3 * RECTSIZE)), RECTSIZE, RECTSIZE))
for i in range (0, 20):
    pygame.draw.rect(windowSurface, RED, (RECTSIZE + (i * 2 * RECTSIZE), (DISPLAY[1] - (3 * RECTSIZE)), RECTSIZE, RECTSIZE))

#left line
for i in range (0, 13):
    pygame.draw.rect(windowSurface, RED, (0, (DISPLAY[1] - (4 * RECTSIZE) - (i * 2 * RECTSIZE)), RECTSIZE, RECTSIZE))
for i in range (0, 13):
    pygame.draw.rect(windowSurface, WHITE, (0, (DISPLAY[1] - (5 * RECTSIZE) - (i * 2 * RECTSIZE)), RECTSIZE, RECTSIZE))

#right line
for i in range (0, 13):
    pygame.draw.rect(windowSurface, WHITE, (DISPLAY[0] - RECTSIZE, (DISPLAY[1] - (4 * RECTSIZE) - (i * 2 * RECTSIZE)), RECTSIZE, RECTSIZE))
for i in range (0, 13):
    pygame.draw.rect(windowSurface, RED, (DISPLAY[0] - RECTSIZE, (DISPLAY[1] - (5 * RECTSIZE) - (i * 2 * RECTSIZE)), RECTSIZE, RECTSIZE))

#top line left
for i in range (0, 9):
    pygame.draw.rect(windowSurface, RED, (0 + (i * 2 * RECTSIZE), 0, RECTSIZE, RECTSIZE))
for i in range (0, 9):
    pygame.draw.rect(windowSurface, WHITE, (RECTSIZE + (i * 2 * RECTSIZE), 0, RECTSIZE, RECTSIZE))

#top line right
for i in range (0, 9):
    pygame.draw.rect(windowSurface, RED, (22 * RECTSIZE + (i * 2 * RECTSIZE), 0, RECTSIZE, RECTSIZE))
for i in range (0, 9):
    pygame.draw.rect(windowSurface, WHITE, (23 * RECTSIZE + (i * 2 * RECTSIZE), 0, RECTSIZE, RECTSIZE))

#Platform
FONTSIZE = int(75 * XVALUE/2046)
basicFont = pygame.font.SysFont(None, FONTSIZE)
platformNo = basicFont.render('1', True, BLACK, BLUEGREEN)
platformRect = platformNo.get_rect()
platformRect.left = RECTSIZE * 19
platformRect.top = DISPLAY[1] - (4 * RECTSIZE)
platformRect.size = (RECTSIZE * 20, RECTSIZE)

pygame.draw.rect(windowSurface, BLUEGREEN, (RECTSIZE * 12, (DISPLAY[1] - (4 * RECTSIZE)), RECTSIZE * 15, RECTSIZE))
pygame.draw.polygon(windowSurface, BLUEGREEN, ((RECTSIZE * 11, DISPLAY[1] - (3 * RECTSIZE)), (RECTSIZE * 12, DISPLAY[1] - (4 * RECTSIZE)), (RECTSIZE * 12, DISPLAY[1] - (3 * RECTSIZE))))
pygame.draw.polygon(windowSurface, BLUEGREEN, ((RECTSIZE * 28, DISPLAY[1] - (3 * RECTSIZE)), (RECTSIZE * 27, DISPLAY[1] - (4 * RECTSIZE)), (RECTSIZE * 27, DISPLAY[1] - (3 * RECTSIZE))))
#pygame.draw.circle(windowSurface, PURPLE, (500, 120), 7, 0)
#pygame.draw.circle(windowSurface, PURPLE, PORCIRCLETHREE, 7, 0)

#pygame.draw.rect(windowSurface, WHITE, (485, 125, 12, 12)
#pygame.draw.polygon(windowSurface, RED, ((484, 125), (472, 137), (484, 137)))
#pygame.draw.polygon(windowSurface, WHITE, ((472, 138), (472, 150), (484, 138)))
#pygame.draw.polygon(windowSurface, RED, ((12, 0), (0, 12), (12, 12)))
#pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

#pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380] = YELLOW
del pixArray

windowSurface.blit(platformNo, platformRect)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
