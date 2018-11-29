
import pygame
import random

from quadtree import QuadTree, RectData


def draw_quadtree(surface, node):
    for n in node.nodes:
        draw_quadtree(surface, n)
        pygame.draw.rect(surface, (192, 192, 192), pygame.Rect(n.x, n.y, n.w + 1, n.h + 1), 1)
        for d in n.data:
            pygame.draw.rect(surface, d.data, pygame.Rect(d.x, d.y, d.w, d.h))
    for d in node.data:
        pygame.draw.rect(surface, d.data, pygame.Rect(d.x, d.y, d.w, d.h))



display = pygame.display.set_mode((640, 640))
clock = pygame.time.Clock()

mdown = False
mx1 = 0
my1 = 0
mx2 = 0
my2 = 0
selected = []

quadtree = QuadTree(8, 640, 640)

keep_going = True
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x = random.randint(0, 600)
                y = random.randint(0, 600)
                w = random.randint(3, 40)
                h = random.randint(3, 40)
                color = (random.randint(64, 250), random.randint(64, 250), random.randint(64, 250))
                quadtree.add(RectData(x, y, w, h, color))

                mx1, my1, mx2, my2 = (0, 0, 0, 0)
                mdown = False
                selected = []

            if event.key == pygame.K_b:
                for d in selected:
                    quadtree.remove(d)
                selected = []

            if event.key == pygame.K_c:
                quadtree.clear()
                mx1, my1, mx2, my2 = (0, 0, 0, 0)
                mdown = False
                selected = []

        if event.type == pygame.MOUSEBUTTONDOWN:
            mdown = True
            mx1, my1 = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            mdown = False

            if mx2 < mx1:
                mx1, mx2 = mx2, mx1

            if my2 < my1:
                my1, my2 = my2, my1

            selected = [rect for rect in quadtree.querry(mx1, my1, mx2 - mx1, my2 - my1)]

    if mdown:
        mx2, my2 = pygame.mouse.get_pos()

    display.fill((255, 255, 255))
    draw_quadtree(display, quadtree.root)

    pygame.draw.rect(display, (255, 0, 0), pygame.Rect(mx1, my1, mx2 - mx1, my2 - my1), 1)

    for d in selected:
        pygame.draw.rect(display, (0, 0, 0), pygame.Rect(d.x, d.y, d.w, d.h), 2)

    pygame.display.flip()

    clock.tick(60)
