from OpenGL.GL import *
import scipy.misc

class Texture:

    def __init__(self, tex_id):
        self.id = tex_id


    def bind(self, texture_slot = GL_TEXTURE0):
        glActiveTexture(texture_slot)
        glBindTexture(GL_TEXTURE_2D, self.id)

    @staticmethod
    def load2D(filename, filtering = GL_LINEAR, wrap = GL_CLAMP):
        data_mat = scipy.misc.imread(filename)
        data_arr = []
        w = len(data_mat)
        h = len(data_mat[0])
        for x in data_mat:
            for y in x:
                for pix in y:
                    data_arr.append(pix)

        return Texture(Texture.internal_load_from_list(data_arr, w, h, filtering, wrap))

    @staticmethod
    def internal_load_from_list(data, w, h, filtering, wrap):
        id = glGenTextures(1)

        glBindTexture(GL_TEXTURE_2D, id)

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, wrap)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, wrap)

        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, filtering)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, filtering)

        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, w, h, 0, GL_RGBA, GL_UNSIGNED_BYTE, data)

        return id

