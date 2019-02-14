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
    for l in matrix:
        printMatrix += str(l[tmp]) + "  "
        tmp += 1
        if tmp >= len(matrix) - 1:
            printMatrix += "\n"
            tmp = 0
    for l in matrix:
        printMatrix += '1  '

    print (printMatrix)


#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    diagonal = 0
    for i in matrix:
        for ele in i:
            if ele == diagonal:
                i[ele] = 1
            else:
                i[ele] = 0
        diagonal += 1
        
    print_matrix(matrix)
    

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    #copy over m2
    cols = []
    for i in m2:
        for a in m1:
            
    

    
    tmp = new_matrix()
    

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

