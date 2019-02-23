from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()


draw_lines( matrix, screen, color )
display(screen)

#functions to test:
print_matrix( matrix )

add_point( matrix, 1, 1, 1 )
add_edge( matrix, 2, 2, 2, 3, 3, 3 )

matrix = new_matrix()
ident( matrix )
#ident( matrix )
#matrix_mult( m1, m2 )

#draw_lines( matrix, screen, color )
#add_edge( matrix, x0, y0, z0, x1, y1, z1 )
#add_point( matrix, x, y, z=0 )
