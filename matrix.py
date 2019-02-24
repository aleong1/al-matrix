"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    tmp = 0
    printMatrix = ''
    while tmp < len(matrix[0]):
        for l in matrix:  #cols
            printMatrix += str(l[tmp]) + "  "
        printMatrix +="\n"
        tmp += 1
    print (printMatrix)


#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    diagonal = 0
    r = 0
    while r < len(matrix):
        c = 0
        while c < len(matrix):
            if c == diagonal:
                matrix[r][c] = 1.00
            else:
                matrix[r][c] = 0.00
            c+=1
        diagonal += 1
        r+=1


#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    m = []
    for i in m2:
        col = []
        c = 0
        while c < len(m1[0]):
            r = 0
            sum = 0
            while r < len(m1):
                sum += i[r]*m1[r][c]
                r += 1
            col.append(sum)
            c += 1
        m.append(col)

    cols = 0   #empty m2
    l = len(m2)
    while cols < l:
        del m2[0]
        cols += 1

    for a in m:
        m2.append(a)


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
