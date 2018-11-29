

# Import a library of functions called 'pygame'
import pygame
import math
# Initialize the game engine
pygame.init()

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

WHITE = (0xFF, 0xFF, 0xFF)

HEIGHT=700
WIDTH =500
size = (HEIGHT, WIDTH)
screen = pygame.display.set_mode(size)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
time=0
# Speed in pixels per frame
x_speed = 0
y_speed = 0

# Current position
x_coord = 10
y_coord = 10
y_coord = 10


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

        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
                y_speed = 0

    # --- Game logic should go here

    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, [350, 200, 200, 250],  0)

    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)

    for i in range(20):
        radians_x = i / 20
        radians_y = i / 6

        x = int(75 * math.sin(radians_x)) + 200
        y = int(75 * math.cos(radians_y)) + 200

        pygame.draw.line(screen, BLACK, [x, y], [x + 5, y], 5)

    for x_offset in range(30, 300, 30):
        pygame.draw.line(screen, BLACK, [x_offset, 100], [x_offset - 10, 90], 2)
        pygame.draw.line(screen, BLACK, [x_offset, 90], [x_offset - 10, 100], 2)

    # Draw a rectangle
    pygame.draw.rect(screen, BLACK, [20, 20, 250, 100], 2)

    # This draws a triangle using the polygon command
    pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)

    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)

    # Render the text. "True" means anti-aliased text. (Interesting... what is aliasing?)
    # Black is the color. The variable BLACK was defined
    # above as a list of [0, 0, 0]
    # Note: This line creates an image of the letters,
    # but does not put it on the screen yet.
    text = font.render("My text", True, BLACK)

    # Put the image of the text on the screen at 250x250
    screen.blit(text, [250, 250])

    score =time

    text = font.render("Score: " + str(score), True, BLACK)

    screen.blit(text, [WIDTH, HEIGHT/2])

    pygame.draw.polygon(screen, BLACK, [[HEIGHT, 0], [0, 0], [0, WIDTH]], 5)
    pygame.draw.polygon(screen, BLACK, [[HEIGHT, WIDTH], [HEIGHT/2, WIDTH], [HEIGHT, WIDTH/2]], 5)


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    time+=1
    clock.tick(60)