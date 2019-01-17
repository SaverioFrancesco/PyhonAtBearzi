import numpy as numpy
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

from math import *


# ----------------------------------------------------------------#
def main():
    a = -10.0
    t = 0.0
    r = 0.0
    movea = False
    movet = False
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glEnable(GL_DEPTH_TEST);

    glDepthFunc(GL_LESS);

    program = glCreateProgram()
    vertex = glCreateShader(GL_VERTEX_SHADER)
    fragment = glCreateShader(GL_FRAGMENT_SHADER)

    # In GLSL, built-in variables like gl_ModelViewProjectionMatrix or functions like ftransform()
    ## are deprecated - that's right, but that's only because the whole matrix stack is deprecated
    ## in GL 3.x and you're supposed to use your own matrix stack

    vertex_code = """
    
    uniform mat4   modelview; 
uniform mat4   projection;    // Projection matrix
        uniform float theta;
        uniform vec4 blue;
      attribute vec2 position;
      attribute vec4 color;
        varying vec4 v_color;
      void main() { 
        float ct = cos(theta);
        float st = sin(theta);
        float x = 0.75* (position.x*ct - position.y*st);
        float y = 0.75* (position.x*st + position.y*ct);
        gl_Position =   projection *  modelview * vec4(x, y, 0.0, 1.0);
        v_color = color;
      } """

    fragment_code = """
    uniform vec4 blue;
       varying vec4 v_color;
       void main() { gl_FragColor = v_color+blue/2.0; } """

    # Build data
    # --------------------------------------
    data = np.zeros(4, [("position", np.float32, 2),
                        ("color", np.float32, 4)])
    data['position'] = (-1, +1), (+1, +1), (-1, -1), (+1, -1)
    data['color'] = (0, 1, 0, 1), (1, 1, 0, 1), (1, 0, 0, 1), (0, 0, 1, 1)

    # Set shaders source
    glShaderSource(vertex, vertex_code)
    glShaderSource(fragment, fragment_code)

    # Compile shaders
    glCompileShader(vertex)
    if not glGetShaderiv(vertex, GL_COMPILE_STATUS):
        error = glGetShaderInfoLog(vertex).decode()
        print(error)
        raise RuntimeError("Vertex shader compilation error")

    glCompileShader(fragment)
    if not glGetShaderiv(fragment, GL_COMPILE_STATUS):
        error = glGetShaderInfoLog(fragment).decode()
        print(error)
        raise RuntimeError("Fragment shader compilation error")

    glAttachShader(program, vertex)
    glAttachShader(program, fragment)
    glLinkProgram(program)

    if not glGetProgramiv(program, GL_LINK_STATUS):
        print(glGetProgramInfoLog(program))
        raise RuntimeError('Linking error')

    glDetachShader(program, vertex)
    glDetachShader(program, fragment)

    glUseProgram(program)

    # ----------------------------

    def draw():

        #ANCORA....
        mvm = (GLfloat * 16)()
        glGetFloatv(GL_MODELVIEW_MATRIX, mvm);

        loc = glGetUniformLocation(program, "modelview")
        glUniformMatrix4fv(loc, 1, GL_FALSE, mvm)

        loc = glGetUniformLocation(program, "projection")
        glUniformMatrix4fv(loc, 1, GL_FALSE, proj)

        glDrawArrays(GL_TRIANGLE_STRIP, 0, 4)

    # Build buffer
    # --------------------------------------

    # Request a buffer slot from GPU
    buffer = glGenBuffers(1)

    # Make this buffer the default one
    glBindBuffer(GL_ARRAY_BUFFER, buffer)

    # Upload data
    glBufferData(GL_ARRAY_BUFFER, data.nbytes, data, GL_DYNAMIC_DRAW)

    # Bind the position attribute
    # --------------------------------------
    stride = data.strides[0]
    offset = ctypes.c_void_p(0)
    loc = glGetAttribLocation(program, "position")
    glEnableVertexAttribArray(loc)
    glBindBuffer(GL_ARRAY_BUFFER, buffer)
    glVertexAttribPointer(loc, 2, GL_FLOAT, False, stride, offset)

    # Upload the varyng color
    # --------------------------------------

    offset = ctypes.c_void_p(data.dtype["position"].itemsize)  # skip the previous part
    loc = glGetAttribLocation(program, "color")
    glEnableVertexAttribArray(loc)
    glBindBuffer(GL_ARRAY_BUFFER, buffer)
    glVertexAttribPointer(loc, 4, GL_FLOAT, False, stride, offset)

    # Upload the uniform color
    # --------------------------------------
    loc = glGetUniformLocation(program, "blue")
    glUniform4f(loc, 0.0, 0.0, 1.0, 1.0)

    time = 0.0
    loc = glGetUniformLocation(program, "theta")
    glUniform1f(loc, time)

    proj = (GLfloat * 16)()
    glGetFloatv(GL_PROJECTION_MATRIX, proj);

    mvm = (GLfloat * 16)()
    glGetFloatv(GL_MODELVIEW_MATRIX, mvm);

    loc = glGetUniformLocation(program, "modelview")
    glUniformMatrix4fv(loc, 1, GL_FALSE, mvm)

    loc = glGetUniformLocation(program, "projection")
    glUniformMatrix4fv(loc, 1, GL_FALSE, proj)

    # glShadeModel(GL_SMOOTH)
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

        time += 0.03
        loc = glGetUniformLocation(program, "theta")
        glUniform1f(loc, time)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();

        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
        # glLoadIdentity()

        # glOrtho(-40.0, 40.0, -40.0, 40.0, -40.0, 40.0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        #gluLookAt(4.0, 0.0, 10.0, 2.0, 4.0, -3.0, 2.0, 2.0, -1.0)

        r += 0.9

        glRotatef(r, 1, 1, 1)


        draw()

        glRotatef(-r, 1, 1, 1)


        draw()

        pygame.display.flip()

        pygame.time.wait(10)


if __name__ == '__main__':
    main()
