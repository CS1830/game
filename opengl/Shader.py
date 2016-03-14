from OpenGL.GL import *

class Shader:

    def __init__(self, load_file):
        self.program = glCreateProgram()
        self.name = load_file
        self.loadShaderStrings(load_file)

    def loadShaderStrings(self, load_file):
        vst = ""
        fst = ""
        vsf = open(load_file + ".vert")
        fsf = open(load_file + ".frag")
        for line in vsf: vst += line
        for line in fsf: fst += line
        self.attachShader(GL_VERTEX_SHADER, vst)
        self.attachShader(GL_FRAGMENT_SHADER, fst)
        self.compileShader()

    def attachShader(self, enum_target, source):
        shader = glCreateShader(enum_target)

        if not shader: raise Exception("Failled to malloc shader location for shader: " + self.name
                                    + ("GL_VERTEX_SHADER" if enum_target is GL_VERTEX_SHADER else "GL_FRAGMENT_SHADER"))

        glShaderSource(shader, source)
        glCompileShader(shader)

        if not glGetShaderiv(shader, GL_COMPILE_STATUS):
            print (self.name + " " + ("GL_VERTEX_SHADER" if enum_target is GL_VERTEX_SHADER else "GL_FRAGMENT_SHADER")
                             + "\n" + glGetShaderInfoLog(shader))

        glAttachShader(self.program, shader)

    def compileShader(self):

        glLinkProgram(self.program)

        if not glGetProgramiv(self.program, GL_LINK_STATUS):
            print (self.name + " [LINKING] " + glGetProgramInfoLog(self.program))

        glValidateProgram(self.program)

        if not glGetProgramiv(self.program, GL_VALIDATE_STATUS):
            print (self.name + " [VALIDATION] " + glGetProgramInfoLog(self.program))



    def bind(self):
        glUseProgram(self.program)