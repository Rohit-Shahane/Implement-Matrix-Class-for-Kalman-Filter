import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I


    
class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        determinant = 1/((self[0][0]*self[1][1])-(self[0][1]*self[1][0]))
        return determinant
    
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
        # TODO - your code here
        total=0
        for i in range(self.h):
            for j in range(self.w):
                if(i==j):
                    total=total + self[i][j]
                    trance=total
        return trance
                        
                           
                               
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        if self.h == 1 and self.w==1:
            temp=[]
            temp.append([1/self[0][0]])
            return Matrix(temp)
    
        elif self.h==2 and self.w==2:
            inv = zeroes(2, 2)    
            den = self.determinant()
            new = [[self[1][1],-self[0][1]],[-self[1][0], self[0][0]]]
            for i in range(self.h):
                for j in range(self.w):
                    inv[i][j] = den * new[i][j]
            return inv

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        m_transpose=[]
        for j in range(self.w):
            row=[]
            for i in range(self.h):
                row.append(self[i][j])
            m_transpose.append(row)
        return Matrix(m_transpose)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        mSum=[]
        row=[]
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self[i][j] + other[i][j])
            mSum.append(row)
        return Matrix(mSum)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        r=[]
        for i in range(self.h):
            #row=self[i]
            new_row=[]
            for j in range(self.w):
                s=self[i][j]
                news=-1*s
                new_row.append(news)
            r.append(new_row)
        return Matrix(r)
                           

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        mSubt=[]
        row=[]
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self[i][j] - other[i][j])
            mSubt.append(row)
        return Matrix(mSubt)
    
    def dot_product(self, vector_one,vector_two):
        
        result = 0
        
        for i in range(len(vector_one)):
            result += vector_one[i] * vector_two[i]
        return result
    
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        
        product = [] 
        tr = other.T()
        for i in range(self.h):
            dot=[]
            for j in range(tr.h):
                dot.append(self.dot_product(self.g[i],tr.g[j]))
            product.append(dot)
        return Matrix(product)

    


    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        product = [] 
        for i in range(self.h):
            dot=[]
            for j in range(self.w):
                dot.append(self[i][j] * other)
            product.append(dot)
        return Matrix(product)
