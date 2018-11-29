# Import a library of functions called 'pygame'
import pygame
from SpriteBlockpy import *
import random
# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

WHITE = (0xFF, 0xFF, 0xFF)

size = (640, 640)
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


t, t1 = 0, 0
time = 0

CollisionDetention.buildStructure(640, 640)

pupp = Puppet(pygame,2,2)

#tile = Tile(pygame)

pipe= Pipe(pygame, 500,500)

wall = Wall(pygame, 1, 300)

floar1 = Floar(pygame, 200, 200)

floar2 = Floar(pygame, 100, 100)

floar3 = Floar(pygame, 400, 200)

floar4 = Floar(pygame, 400, 300)

floar5 = Floar(pygame, 50, 300)

CollisionDetention.register(pupp)
CollisionDetention.register(pipe)
CollisionDetention.registerCompaund(wall)
CollisionDetention.registerCompaund(floar1)
CollisionDetention.registerCompaund(floar2)
CollisionDetention.registerCompaund(floar3)
CollisionDetention.registerCompaund(floar4)
CollisionDetention.registerCompaund(floar5)


randomPieces=[]
for u in range(0, 100):
    randomPieces.append(Pipe(pygame, random.randint(1, 600),random.randint(1, 500),Pipe.BOT))

for i in randomPieces:
    CollisionDetention.register(i)



CollisionDetention.insertRegistred()

jump=False
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
            elif event.key == pygame.K_j:
                jump=True

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
            elif event.key == pygame.K_j:
                jump=False

    # --- Game logic should go here

    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    x_coord += x_speed
    y_coord += y_speed

    CollisionDetention.moveObject(pupp,x_speed,0)
    CollisionDetention.moveObject(pupp,0,y_speed)


    if not jump:
        CollisionDetention.moveObject(pupp, 0, 0.981 / 2)
        CollisionDetention.moveObject(pupp, 0, 0.981 / 2)
    else:
        CollisionDetention.moveObject(pupp, 0, 0.981 / 4)
        CollisionDetention.moveObject(pupp, 0, 0.981 / 4)

    pupp.tick()#animation
    pupp.draw(screen)

    
    #tile.setPosition(200, 100)
    #tile.draw(screen)


    wall.draw(screen)
    floar1.draw(screen)
    floar2.draw(screen)
    floar3.draw(screen)
    floar4.draw(screen)
    floar5.draw(screen)
    pipe.draw(screen)

    for i in randomPieces:
        i.draw(screen)

   # CollisionDetention.draw(pygame, screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    time += 1
    clock.tick(60)
