# Pygame sprite Example
import pygame
import random
import os

WIDTH = 400
HEIGHT = 300
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set up assets folders
# Windows: "C:\Users\chris\Documents\img"
# Mac: "/Users/chris/Documents/img"
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "Sprites")

import pygame, sys
from pygame.locals import *

dd = pygame.transform.scale2x


def sprite_sheetList(listOfOfsets, file):
    # Initial Values
    sheet = pygame.image.load(file).convert()  # Load the sheet
    sheet_rect = sheet.get_rect()
    sprites = []

    for coord in listOfOfsets:
        len_sprt_x, len_sprt_y = coord[2], coord[3]  # sprite size
        sprt_rect_x, sprt_rect_y = coord[0], coord[1]  # where to find first sprite on sheet

        sheet.set_clip(pygame.Rect(sprt_rect_x, sprt_rect_y, len_sprt_x, len_sprt_y))  # find sprite you want
        sprite = sheet.subsurface(sheet.get_clip())  # grab the sprite you want

        sprites.append(dd((sprite)))

    # print(sprites)
    return sprites


class Player(pygame.sprite.Sprite):
    # sprite for the Player
    WALK = 0
    STAND = 1

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.y_speed = 5

        coordList = [(113, 6, 18, 34), (138, 6, 18, 34), (163, 6, 18, 34), (189, 6, 18, 34),
                     (96, 165, 25, 35),
                     (128, 165, 25, 35),
                     (158, 165, 25, 35),
                     (185, 165, 25, 35),
                     (185, 165, 25, 35),
                     (239, 165, 25, 35),
                     (266, 165, 25, 35),
                     (294, 165, 25, 35),
                     (322, 165, 25, 35),
                     (351, 165, 25, 35),
                     (380, 165, 25, 35),
                     (410, 165, 25, 35),
                     (441, 165, 29, 35),
                     (473, 165, 29, 35),
                     (506, 165, 29, 35),
                     (538, 165, 29, 35),
                     (570, 165, 29, 35)
                     ]
        self.speedRun = [1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

        self.possibleSprites = sprite_sheetList(coordList, os.path.join(img_folder, "hero.png"))

        for i in self.possibleSprites:
            i.set_colorkey(i.get_at((1, 1)))

        self.image = self.possibleSprites[0]
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.ofset_x = self.rect.x
        self.ofset_y = self.rect.y

        self.turn = True
        self.timer = 0

        self.index = 0
        self.flip = False

        self.speed = 10

        self.stopWalking()

    def nextStand(self, n):

        return (n + 1) % 4

    def nextWalk(self, n):

        r = n - 4
        return 4 + ((r + 1) % 17)

    def update(self):

        if self.turn:
            self.turn = False

            if self.CHARAPTER_STATE == self.__class__.STAND:
                self.SpriteID = self.nextStand(self.SpriteID)
                self.image = pygame.transform.flip(self.possibleSprites[self.SpriteID], self.flip, False)
            elif self.CHARAPTER_STATE == self.__class__.WALK:

                self.SpriteID = self.nextWalk(self.SpriteID)
                # self.rect.x
                self.ofset_x += (-1 if self.flip else 1) * self.speed * self.speedRun[self.SpriteID - 4]
                self.image = pygame.transform.flip(self.possibleSprites[self.SpriteID], self.flip, False)

        else:
            self.timer += 1
            if self.timer == 1:
                self.timer = 0
                self.turn = True

    def startWalking(self, flip=False):
        self.CHARAPTER_STATE = self.__class__.WALK
        self.flip = flip
        self.SpriteID = 16

    def stopWalking(self):
        self.CHARAPTER_STATE = self.__class__.STAND
        self.SpriteID = 0


# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF, 32)
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

background = pygame.image.load(os.path.join(img_folder, "hall.png")).convert()

x_shift = 0
y_shift = 0
# Game loop
running = True

pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)

while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                player.startWalking(True)
                x_shift += 10
            elif event.key == pygame.K_RIGHT:
                player.startWalking(False)
                x_shift -= 10
        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                player.stopWalking()

            elif event.key == pygame.K_RIGHT:
                player.stopWalking()

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(WHITE)

    textsurface = myfont.render('Sprite :: '+ str(player.SpriteID), False, WHITE)

    screen.blit(dd(background), (-player.ofset_x - 300, -player.ofset_y - 300))

    screen.blit(textsurface, (0, 0))


    # player.image.blit(screen, (player.rect.x,player.rect.y ))
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
