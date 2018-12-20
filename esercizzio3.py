# KidsCanCode - Game Development with Pygame video series
# Shmup game - part 4
# Video link: https://www.youtube.com/watch?v=mOckdKp3V38
# Adding graphics
import pygame
import random
from os import path

import pypybox2d

print(dir(pypybox2d))

img_dir = path.join(path.dirname(__file__), 'Sprites')

WIDTH = 480
HEIGHT = 600
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(( HEIGHT, WIDTH))
pygame.display.set_caption("Shmup!")
clock = pygame.time.Clock()



class Ball(pygame.sprite.Sprite):
    def __init__(self, r):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((r, r))
        self.image.set_colorkey(BLACK)
        self.image.fill(BLACK)
        #pygame.draw.circle(self.image,GREEN,(r//2,r//2),r//2,1)
        self.rect = self.image.get_rect()
        self.rect.center = (  random.randint(r//2,WIDTH-r) ,  random.randint(r//2,HEIGHT-r))

        self.speedx = random.randint(-1,1)
        self.speedy = random.randint(-1,1)

        self.vicini=[]

    def update(self):
        self.rect.x +=  self.speedx
        self.rect.y += self.speedy

class Wall(pygame.sprite.Sprite):
    def __init__(self, x,y,h,w):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((h,w))
        self.image.set_colorkey(BLACK)
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x =x
        self.rect.y = y


    def update(self):
        pass


# Load all game graphics

all_sprites = pygame.sprite.Group()

balls = pygame.sprite.Group()
walls = pygame.sprite.Group()

for i in range(0,100):
    t= Ball(30)
    all_sprites.add(t)
    balls.add(t)

for b in balls:
    for c in balls:
        if not c is b:
            if not b in c.vicini:
                if random.randint(0,200)==1:
                    b.vicini.append(c)

west= Wall(0,0,3,WIDTH)
walls.add(west)
all_sprites.add(west)

nord= Wall(0,0,HEIGHT,3)
walls.add(nord)
all_sprites.add(nord)

sud= Wall(0,WIDTH-3,HEIGHT,3)
walls.add(sud)
all_sprites.add(sud)

est= Wall(HEIGHT-3,0,3,WIDTH)
walls.add(est)
all_sprites.add(est)

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

     #screen.fill(BLUE)

    all_sprites.draw(screen)

    for ball1 in balls:
        for ball2 in balls:
            if (not ball1 is ball2) and ( ball2 in ball1.vicini ):
                pygame.draw.aaline(screen,RED,ball1.rect.center,ball2.rect.center)

    # check to see if a bullet hit a mob
    #hits = pygame.sprite.groupcollide(balls, walls, False, False)
    #for hit in hits:


    # check to see if a mob hit the player
    for ball in balls:
        copy = balls.copy()
        copy.remove(ball)
        hits = pygame.sprite.spritecollide(ball,copy , False)
        if hits:
            ball.rect.x -=ball.speedx
            ball.speedx =-ball.speedx


    for ball in balls:

        rollbackX= False
        rollbackY = False

        hits = pygame.sprite.spritecollide(ball,[west, est] , False)
        if hits:
            ball.speedx =-ball.speedx
            rollbackX= True

        hits = pygame.sprite.spritecollide(ball,[nord, sud] , False)
        if hits:
            ball.speedy = -ball.speedy
            rollbackY=True

        if rollbackX:
            ball.rect.x += ball.speedx
        if rollbackY:
            ball.rect.y += ball.speedy

    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()