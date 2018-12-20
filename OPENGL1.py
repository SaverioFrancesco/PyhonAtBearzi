import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)


def Quad():

    #glScalef(3.0, 30.0, 3.0)
    glBegin(GL_QUADS)
    glVertex3f(-1.0, -1.0, 0.0)
    glColor3f(0, 0, 1)
    glVertex3f(1.0, -1.0, 0.0)
    glColor3f(1, 0, 0)
    glVertex3f(1.0, 1.0, 0.0)
    glColor3f(0, 1, 0)
    glVertex3f(-1.0, 1.0, 0.0)
    glEnd()


def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    a = 0.0
    t = 0.0
    movea = False
    movet = False
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glDisable(GL_LIGHTING)  # context lights by default
    glEnable(GL_CULL_FACE)
    glCullFace(GL_BACK)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_a:
                    print("a")
                    movea = True
                if event.key == K_t:
                    print("t")
                    movet = True
            if event.type == KEYUP:
                if event.key == K_a:
                    print("a")
                    movea = False
                if event.key == K_t:
                    print("t")
                    movet = False

        if movea: a += 0.1
        if movet: t += 1.0


        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();

        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
        #glLoadIdentity()

        #glOrtho(-40.0, 40.0, -40.0, 40.0, -40.0, 40.0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        #gluLookAt(4.0, 0.0, 10.0, 2.0, 4.0, -3.0, 2.0, 2.0, -1.0)

        glPushMatrix()
        glPopMatrix()
        glTranslatef(0.0, 0.0, -5)

        glTranslatef(0.0, 0.0, a)

        glRotatef(t, 1 , 0, 0)


        Cube()

        #Quad()

        pygame.display.flip()
        pygame.time.wait(10)


main()
