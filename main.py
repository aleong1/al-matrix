from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()


draw_lines( matrix, screen, color )
display(screen)

#functions to test:
add_edge( matrix, 1,2,3,4, 5, 6)
print_matrix(matrix)

m1 = new_matrix()
ident( m1 )
print_matrix(m1)

matrix_mult( m1, matrix )

m3 = new_matrix()
add_edge(m3, 1,2,3,4,5,6)
add_edge(m3, 7,8,9,10,11,12)
print_matrix(m3)

matrix_mult(m3, matrix)
print_matrix(matrix)
