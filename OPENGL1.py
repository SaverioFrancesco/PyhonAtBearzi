import numpy as numpy
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import numpy

from math import *

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


# Draw a sphere
def sphere():
    lats = 20
    longs = 20

    for i in range(0, lats + 1):
        lat0 = pi * (-0.5 + float(float(i - 1) / float(lats)))
        z0 = sin(lat0)
        zr0 = cos(lat0)

        lat1 = pi * (-0.5 + float(float(i) / float(lats)))
        z1 = sin(lat1)
        zr1 = cos(lat1)

        # Use Quad strips to draw the sphere
        glBegin(GL_QUAD_STRIP)
        # glBegin(GL_LINE_STRIP)

        for j in range(0, longs + 1):
            lng = 2 * pi * float(float(j - 1) / float(longs))
            x = cos(lng)
            y = sin(lng)
            glNormal3f(x * zr0, y * zr0, z0)
            glVertex3f(x * zr0, y * zr0, z0)
            glColor3f(20 * x * zr0 % 255, 20 * y * zr0 % 255, 20 * z0 % 255)
            glNormal3f(x * zr1, y * zr1, z1)
            glVertex3f(x * zr1, y * zr1, z1)
            glColor3f(20 * x * zr1, 20 * y * zr1, 20 * z1)

        glEnd()


def Quad():
    # glScalef(3.0, 30.0, 3.0)
    glBegin(GL_QUADS)
    glVertex3f(-1.0, -1.0, 0.0)
    glColor3f(0, 0, 1)
    # glNormal3f(0.0,0.0,1.0)

    glVertex3f(1.0, -1.0, 0.0)
    glColor3f(1, 0, 0)
    # glNormal3f(0.0,0.0,1.0)

    glVertex3f(1.0, 1.0, 0.0)
    glColor3f(0, 1, 0)
    # glNormal3f(0.0,0.0,1.0)

    glVertex3f(-1.0, 1.0, 0.0)
    # glColor3f(1, 1, 0)
    # glNormal3f(0.0,0.0,1.0)

    glEnd()

def Cube2():
    glCullFace(GL_BACK)
    glBegin(GL_QUADS);
    glColor3f(0.0, 1.0, 0.0);
    glVertex3f(1.0, 1.0, -1.0);
    glVertex3f(-1.0, 1.0, -1.0);
    glVertex3f(-1.0, 1.0, 1.0);
    glVertex3f(1.0, 1.0, 1.0);

    glColor3f(1.0, 0.5, 0.0);
    glVertex3f(1.0, -1.0, 1.0);
    glVertex3f(-1.0, -1.0, 1.0);
    glVertex3f(-1.0, -1.0, -1.0);
    glVertex3f(1.0, -1.0, -1.0);

    glColor3f(1.0, 0.0, 0.0);
    glVertex3f(1.0, 1.0, 1.0);
    glVertex3f(-1.0, 1.0, 1.0);
    glVertex3f(-1.0, -1.0, 1.0);
    glVertex3f(1.0, -1.0, 1.0);


    glColor3f(1.0, 1.0, 0.0);
    glVertex3f(1.0, -1.0, -1.0);
    glVertex3f(-1.0, -1.0, -1.0);
    glVertex3f(-1.0, 1.0, -1.0);
    glVertex3f(1.0, 1.0, -1.0);

    glColor3f(0.0, 0.0, 1.0);
    glVertex3f(-1.0, 1.0, 1.0);
    glVertex3f(-1.0, 1.0, -1.0);
    glVertex3f(-1.0, -1.0, -1.0);
    glVertex3f(-1.0, -1.0, 1.0);

    glColor3f(1.0, 0.0, 1.0);
    glVertex3f(1.0, 1.0, -1.0);
    glVertex3f(1.0, 1.0, 1.0);
    glVertex3f(1.0, -1.0, 1.0);
    glVertex3f(1.0, -1.0, -1.0);
    glEnd();

    glCullFace(GL_FRONT)

def Cube():
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    a = -10.0
    t = 0.0
    r = 0.0
    movea = False
    movet = False
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glDisable(GL_LIGHTING)  # context lights by default
    # glEnable(GL_LIGHTING)
    glEnable(GL_CULL_FACE)
    glCullFace(GL_FRONT)

    lightZeroPosition = [10., 4., 10., 1.]
    lightZeroColor = [0.8, 1.0, 0.8, 1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    # glEnable(GL_LIGHT0)

    glLightfv(GL_LIGHT1, GL_POSITION, [10.0, 10.0, -10.0, 10.0])

    glLightfv(GL_LIGHT1, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0]);
    glLightfv(GL_LIGHT1, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0]);
    glLightfv(GL_LIGHT1, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0]);

    glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, 0.1);
    glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, 0.05);
    glLightf(GL_LIGHT1, GL_QUADRATIC_ATTENUATION, 0.2);

    # glEnable(GL_LIGHT1)

    # glEnable(GL_COLOR_MATERIAL)
    # glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)

    glEnable(GL_DEPTH_TEST);

    glDepthFunc(GL_LESS);

    #glShadeModel(GL_SMOOTH)

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
        # glLoadIdentity()

        # glOrtho(-40.0, 40.0, -40.0, 40.0, -40.0, 40.0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # gluLookAt(4.0, 0.0, 10.0, 2.0, 4.0, -3.0, 2.0, 2.0, -1.0)

        r += 0.9

        glRotatef(t, 0, 0, 1)

        glPushMatrix()

        glTranslatef(0.0, 0.0, a)

        glRotatef(r, 1, 0, 1)
        Cube()

        # Quad()

        glScale(0.6, 1, 1)
        # sphere()
        glPopMatrix()

        glPushMatrix()

        glTranslatef(0.0, 0.0, -10)

        Cube()
        # glScale(2,2,2)

        # glRotatef(r*r, 1, 1, 1) try it

        glRotatef(3 * r, 1, 0, 0)
        glTranslatef(0.0, 0.0, 3)
        glRotatef(-2 * r, 1, 0, 0)
        # sphere()
        # glutWireSphere(1.0,20,20)

        # glutWireCone(1,1,1)
        # FillCube()

        # sphere()
        Cube2()

        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)


main()
