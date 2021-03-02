class matrix:
    def __init__(self, m=0, n = -1, val = 0):
        self.m = m
        self.n = m if n==-1 else n
        self.data = [val]* (self.m*self.n)

    def get(self, i,j):
        if(i>=self.m or i<0 or j>=self.n or j<0):
            raise Exception("Index Error")
        return self.data  [i * self.n + j]
    
    def set (self, i, j, val):
        if (i<0 or i>= self.m or j<0 or j>=self.n):
            raise Exception ("Index Error")
        self.data[i*self.n+j] = val
    
    def setconst(self, val):
        self.data = [val]* (self.m*self.n)
    
    def setall (self, *val):
        if self.m * self.n != len (val):
            raise Exception ("wrong dimensions")
        self.data[:] = val

    def __str__(self):
        s = "dimension: " + str(self.m) + "x" + str(self.n) +"n"

        for i in range (slef.m):
            for j in range (self.n):
                s+=str(sel.data[i*self.n +j ]).rjust(9)
            s+="\n"
        return s
    
    def __add__(self, mat2):

        if self.m != mat2.m or self.n != mat2.n:
            raise Exception ("Two matrices are of different dimensions")
        res = matrix(self.m, self.n)
        for i in range (self.n*self.m):
            res.data[i] = self.data[i] + mat.data[i]
        return res
