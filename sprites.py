

# Import a library of functions called 'pygame'
import pygame
# Initialize the game engine
pygame.init()

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

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


background=pygame.image.load("Sprites/psygen.png").convert()


image=pygame.image.load("Sprites/Old hero.png").convert()

color = image.get_at((0,0)) #we get the color of the upper-left corner pixel
image.set_colorkey(color)

#image.set_colorkey((0,0,0,1.0))

t, t1 = 0 ,0
time=0
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
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed = 0
            elif event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP:
                y_speed = 0
            elif event.key == pygame.K_DOWN:
                y_speed = 0


    # --- Game logic should go here

    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    x_coord+=x_speed
    y_coord += y_speed

    screen.blit(background, [0,0])

    if time%15==0 :    t+=1

#    t=t%3
#    t1=0

    t = t % 6
    t1 = 1

    OFSET=16*t
    YOFSET = 17 *t1

    X=16
    Y=15
    clip_rect= (X+OFSET,Y+YOFSET,16,16)


    screen.blit(image, [x_coord, y_coord], clip_rect)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    time+=1
    clock.tick(60)