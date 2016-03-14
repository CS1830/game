class Matrix4f:

    # alloc
    def __init__(self, mat = None):
        if mat is None:
            mat = [0.] * 16
        if len(mat) is not 16:
            raise Exception("matrix array given is not of length 16")
        self.mat = mat

    # identity matrix
    def initIdentity(self):
        self.mat[ 0] = 1.
        self.mat[ 5] = 1.
        self.mat[10] = 1.
        self.mat[15] = 1.

    # Orthographic projection matrix
    def initOrtho(self, left, right, bottom, top, near = -1, far = 1):
        self.mat[ 0] = 2. / (right - left)
        self.mat[ 3] = - (right + left) / (right - left)
        self.mat[ 5] = 2. / (top - bottom)
        self.mat[ 7] = - (top + bottom) / (top - bottom)
        self.mat[10] = 2. / (far - near)
        self.mat[11] = - (far + near) / (far - near)
        self.mat[15] = 1.
        return self

    def initTranslation(self, x, y, z):
        self.initIdentity()
        self.mat[ 3] = x
        self.mat[ 7] = y
        self.mat[11] = z
        return self

    def __mul__(self, other):
        ret = Matrix4f()
        ret.mat[ 0] = self.mat[ 0] * other.mat[ 0] + self.mat[ 1] * other.mat[ 4] + self.mat[ 2] * other.mat[ 8] + self.mat[ 3] * other.mat[12]
        ret.mat[ 1] = self.mat[ 0] * other.mat[ 1] + self.mat[ 1] * other.mat[ 5] + self.mat[ 2] * other.mat[ 9] + self.mat[ 3] * other.mat[13]
        ret.mat[ 2] = self.mat[ 0] * other.mat[ 2] + self.mat[ 1] * other.mat[ 6] + self.mat[ 2] * other.mat[10] + self.mat[ 3] * other.mat[14]
        ret.mat[ 3] = self.mat[ 0] * other.mat[ 3] + self.mat[ 1] * other.mat[ 7] + self.mat[ 2] * other.mat[11] + self.mat[ 3] * other.mat[15]
        ret.mat[ 4] = self.mat[ 4] * other.mat[ 0] + self.mat[ 5] * other.mat[ 4] + self.mat[ 6] * other.mat[ 8] + self.mat[ 7] * other.mat[12]
        ret.mat[ 5] = self.mat[ 4] * other.mat[ 1] + self.mat[ 5] * other.mat[ 5] + self.mat[ 6] * other.mat[ 9] + self.mat[ 7] * other.mat[13]
        ret.mat[ 6] = self.mat[ 4] * other.mat[ 2] + self.mat[ 5] * other.mat[ 6] + self.mat[ 6] * other.mat[10] + self.mat[ 7] * other.mat[14]
        ret.mat[ 7] = self.mat[ 4] * other.mat[ 3] + self.mat[ 5] * other.mat[ 7] + self.mat[ 6] * other.mat[11] + self.mat[ 7] * other.mat[15]
        ret.mat[ 8] = self.mat[ 8] * other.mat[ 0] + self.mat[ 9] * other.mat[ 4] + self.mat[10] * other.mat[ 8] + self.mat[11] * other.mat[12]
        ret.mat[ 9] = self.mat[ 8] * other.mat[ 1] + self.mat[ 9] * other.mat[ 5] + self.mat[10] * other.mat[ 9] + self.mat[11] * other.mat[13]
        ret.mat[10] = self.mat[ 8] * other.mat[ 2] + self.mat[ 9] * other.mat[ 6] + self.mat[10] * other.mat[10] + self.mat[11] * other.mat[14]
        ret.mat[11] = self.mat[ 8] * other.mat[ 3] + self.mat[ 9] * other.mat[ 7] + self.mat[10] * other.mat[11] + self.mat[11] * other.mat[15]
        ret.mat[12] = self.mat[12] * other.mat[ 0] + self.mat[13] * other.mat[ 4] + self.mat[14] * other.mat[ 8] + self.mat[15] * other.mat[12]
        ret.mat[13] = self.mat[12] * other.mat[ 1] + self.mat[13] * other.mat[ 5] + self.mat[14] * other.mat[ 9] + self.mat[15] * other.mat[13]
        ret.mat[14] = self.mat[12] * other.mat[ 2] + self.mat[13] * other.mat[ 6] + self.mat[14] * other.mat[10] + self.mat[15] * other.mat[14]
        ret.mat[15] = self.mat[12] * other.mat[ 3] + self.mat[13] * other.mat[ 7] + self.mat[14] * other.mat[11] + self.mat[15] * other.mat[15]
        return ret

    # to string
    def __str__(self, terminate = "\n"):
        return ("[ " + str(self.mat[ 0]) + ",\t" + str(self.mat[ 1]) + ",\t" + str(self.mat[ 2]) + ",\t" + str(self.mat[ 3]) + " ]\n"
                "[ " + str(self.mat[ 4]) + ",\t" + str(self.mat[ 5]) + ",\t" + str(self.mat[ 6]) + ",\t" + str(self.mat[ 7]) + " ]\n"
                "[ " + str(self.mat[ 8]) + ",\t" + str(self.mat[ 9]) + ",\t" + str(self.mat[10]) + ",\t" + str(self.mat[11]) + " ]\n"
                "[ " + str(self.mat[12]) + ",\t" + str(self.mat[13]) + ",\t" + str(self.mat[14]) + ",\t" + str(self.mat[15]) + " ]" + terminate)