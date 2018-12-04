import pygame, time, math


def display_test():
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption('Pygame')
    pygame.mouse.set_visible(0)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 250))

    pxarray = pygame.PixelArray(background)

    # this is called slicing
    # a = [1, 2, 3]
    # b = a[:]        # b is now a new list, with a copy of a
    # a[0] = 10       # so changing the original list doesn't affect b

    # pxarray[:] = (0,0,0)

    # for e in range(1,800):
    #    pxarray[e]=(e%250,e%25,e%150)

    r = 0
    for t in range(1, 300):
        r += 1
        pxarray[int(200 + math.sin(math.radians(t)) * r)][int(200 + math.cos(math.radians(t)) * r)] = (
        255 - t % 250, 255 - t % 25, t % 150)


    pxarray.replace((0,0,200),(0,200,0), 0) # see man pages

    del pxarray  # deliting it will unlock background

    screen.blit(background, (0, 0))
    pygame.display.flip()
    time.sleep(3)


display_test()
