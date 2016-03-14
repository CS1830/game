from OpenGL.GL import *
import numpy

class Vertex2f:

    def __init__(self, *args):
        if len(args) is 2:
            self.data = [args[0].x, args[0].y, args[1].x, args[1].y]
            return
        if len(args) is 4:
            self.data = [args[0], args[1], args[2], args[3]]
            return
        raise Exception("Invalid arguments for Vertex2f (vec2, vec2) and (f, f, f, f) accepted")


class Mesh:

    def __init__(self, vertices, indices):
        self.vbo = glGenBuffers(1)
        self.ibo = glGenBuffers(1)
        self.size = 0
        self.loadVertice(vertices, indices)


    def loadVertice(self, vertices, indices):
        vert_list = None
        ind_list = None

        # since python doesn't allow me to specify fucking function types...
        # i have to MANUALLY check EVERY FUCKING POSSIBLE TYPE... fuck
        if type(vertices) is list and len(vertices) > 0 and type(vertices[0]) is float:
            vert_list = numpy.array(vertices, numpy.float32)

        if type(indices) is list and len(indices) > 0 and type(indices[0]) is int:
            ind_list = numpy.array(indices, numpy.int32)

        if type(vertices) is numpy.ndarray and len(vertices) > 0 and type(vertices[0]) is numpy.float32:
            vert_list = vertices

        if type(indices) is numpy.ndarray and len(indices) > 0 and type(indices[0]) is numpy.int32:
            ind_list = indices

        # hmpf... in C++ i could just use structs...
        if type(vertices) is list and len(vertices) > 0 and isinstance(vertices[0], Vertex2f):
            vertt = []
            for vertex in vertices:
                vertt.append(vertex.data[0])
                vertt.append(vertex.data[1])
                vertt.append(vertex.data[2])
                vertt.append(vertex.data[3])
            vert_list = numpy.array(vertt, numpy.float32)

        if vert_list is None: raise Exception("Invalid vertex list format")
        if ind_list is None: raise Exception("Invalid index list format")

        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ibo)
        glBufferData(GL_ARRAY_BUFFER, vert_list, GL_STATIC_DRAW)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, ind_list, GL_STATIC_DRAW)
        self.size = len(ind_list)

    def draw(self):
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 4 * 4, ctypes.c_void_p(0))
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 4 * 4, ctypes.c_void_p(2 * 4))

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ibo)
        glDrawElements(GL_TRIANGLES, self.size, GL_UNSIGNED_INT, ctypes.c_void_p(0))

    @staticmethod
    def enableAttribs():
        glEnableVertexAttribArray(0)
        glEnableVertexAttribArray(1)

    @staticmethod
    def disableAttribs():
        glDisableVertexAttribArray(0)
        glDisableVertexAttribArray(1)

    @staticmethod
    def load(objfile): pass
        #return Mesh(0, 0, 0)