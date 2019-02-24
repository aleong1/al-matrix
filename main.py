from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 204, 229, 255 ]
matrix = new_matrix()

#functions to test:
add_edge( matrix, 1,2,3,4, 5, 6)
add_point(matrix, 7,7,7)

m1 = new_matrix()
ident( m1 )

matrix_mult( m1, matrix )

print_matrix(matrix)

m3 = new_matrix()
add_edge(m3, 1,2,3,4,5,6)
add_edge(m3, 7,8,9,10,11,12)

matrix_mult(m3, matrix)

draw = new_matrix()
x = 0
y = 0
z = 0
while x < 475 and y < 475:
    add_edge(draw, x, y, z, x+25, y+25,z)
    x += 50
    y += 10

while x > 25 and y > 25:
    add_edge(draw, x, y, z, x-25, y+25,z)
    x -= 50
    y += 10

while x < 475 and y < 475:
    add_edge(draw, x, y, z, x+25, y+25,z)
    x += 50
    y += 10

while x > 25 and y > 25:
    add_edge(draw, x, y, z, x-25, y+25,z)
    x -= 50
    y += 10

while x < 475 and y < 475:
    add_edge(draw, x, y, z, x+25, y+25,z)
    x += 50
    y += 10

draw_lines( draw, screen, color )
display(screen)
save_extension(screen, 'img.png')
