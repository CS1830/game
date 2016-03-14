import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import time
import random

import opengl.Mesh as Mesh
import opengl.Shader as Shader
import opengl.Texture as Texture
import vecmath.Matrix4f as Matrix4f

mat0 = Matrix4f.Matrix4f()
o_s = 8
mat0.initOrtho(-4./3 * o_s, 4./3 * o_s, -1 * o_s, 1 * o_s, -1, 1)

def main():
    pygame.init()
    display = (800,600)
    # pygame.display.set_mode(display)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    mesh = Mesh.Mesh([
        Mesh.Vertex2f(-.5, -.5, 0, 0),
        Mesh.Vertex2f( .5, -.5, 1, 0),
        Mesh.Vertex2f( .5,  .5, 1, 1),
        Mesh.Vertex2f(-.5,  .5, 0, 1),
    ],
    [0, 1, 2, 0, 2, 3])

    shader = Shader.Shader("shaders/test")

    tex = Texture.Texture.load2D("res/textures/test.png")

    dt = 0.
    last_time = time.time()
    total_t = 0.

    # glEnable(GL_BLEND)
    # glBlendFunc(GL_SRC_ALPHA, GL_ONE)

    model = Matrix4f.Matrix4f()
    model.initTranslation(1, 1, 0)

    points = []

    while True:

        cur_t = time.time()
        dt =  cur_t - last_time
        last_time = cur_t
        total_t += dt

        pygame.display.set_caption("FPS " + str(1 / dt))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT)

        Mesh.Mesh.enableAttribs()

        tex.bind()
        shader.bind()
        glUniform1f(glGetUniformLocation(shader.program, "life"), 1)
        glUniformMatrix4fv(glGetUniformLocation(shader.program, "MVP"), 1, True, mat0.mat)
        mesh.draw()
        for p in points:
            p.update(.01)
            if p.life < 0:
                points.remove(p)
            else:
                glUniform1f(glGetUniformLocation(shader.program, "life"), p.life)
                glUniformMatrix4fv(glGetUniformLocation(shader.program, "MVP"), 1, True, (mat0 * Matrix4f.Matrix4f().initTranslation(p.x, p.y, 0)).mat)
                mesh.draw()

        cap = .01
        if total_t > cap:
            total_t -= cap
            points.append(point(random.uniform(-.7, .7), random.uniform(-.7, .7), 2))

        Mesh.Mesh.disableAttribs()

        # pygame.draw.ellipse(display, 0xFFFFFF, (100, 100), (10, 10))

        pygame.display.flip()


class point:

    def __init__(self, x, y, life):
        self.x = 0
        self.y = 0
        self.vx = x
        self.vy = y
        self.life = life
        self.life_total = life

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.life -= dt


main()