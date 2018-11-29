# Import a library of functions called 'pygame'
import pygame
from SpriteBlockpy import *

# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

WHITE = (0xFF, 0xFF, 0xFF)

size = (700, 500)
screen = pygame.display.set_mode(size)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

x_speed = 0
y_speed = 0

# Current position
x_coord = 10
y_coord = 10
y_coord = 10

t, t1 = 0, 0
time = 0

pupp = Puppet(pygame)

tile = Tile(pygame)

wall = Wall(pygame, 0, 0)

floar1 = Floar(pygame, 200, 100)
floar2 = Floar(pygame, 400, 0)

QuadTreeCollisionDetntion.buildStructure(size[0],size[1])

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -3
                pupp.setState(Puppet.PUPPET_RUN)
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
                pupp.setState(Puppet.PUPPET_RUN)
            elif event.key == pygame.K_UP:
                y_speed = -3
                pupp.setState(Puppet.PUPPET_RUN)
            elif event.key == pygame.K_DOWN:
                y_speed = 3
                pupp.setState(Puppet.PUPPET_RUN)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed = 0
                pupp.setState(Puppet.PUPPET_STAND)
            elif event.key == pygame.K_RIGHT:
                x_speed = 0
                pupp.setState(Puppet.PUPPET_STAND)
            elif event.key == pygame.K_UP:
                y_speed = 0
                pupp.setState(Puppet.PUPPET_STAND)

            elif event.key == pygame.K_DOWN:
                y_speed = 0
                pupp.setState(Puppet.PUPPET_STAND)

    # --- Game logic should go here

    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    x_coord += x_speed
    y_coord += y_speed

    # screen.blit(background, [0,0])

    pupp.setPosition(x_coord, y_coord)
    pupp.tick()
    pupp.draw(screen)

    tile.setPosition(200, 100)
    tile.draw(screen)

    wall.setPosition(300, 100)
    wall.draw(screen)
    floar1.draw(screen)
    floar2.draw(screen)

    QuadTreeCollisionDetntion.draw(pygame,screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    time += 1
    clock.tick(60)
