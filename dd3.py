#
# wortels
#
'''
from math import sqrt

num = int(input('geef aantal wortels: '))

# write file
with open('wortels.txt', 'w') as f1:
    for i in range(1, num + 1):
        f1.write("{0} {1}\n".format(str(i), sqrt(i)))

# read file
with open('wortels.txt', 'r') as f2:
    for line in f2:
        print(line, end='')
'''

#
# versleutelen
#
'''
def flip_bits(a):
    b = b'\xFF'
    c = int.from_bytes(a, 'big') ^ int.from_bytes(b, 'big')	# ^ means exclusive OR
    return c.to_bytes(len(a), 'big')

def versleutel_bestand(in_file, out_file):
    with open(in_file, 'rb') as f_in:
        with open(out_file, 'wb') as f_out:
            byte = f_in.read(1)
            while byte:
                f_out.write(flip_bits(byte))
                byte = f_in.read(1)

with open('test_in.dat', 'wb') as f:
    f.write(b'\x00\x80\xF0\xFF')
    
versleutel_bestand('test_in.dat', 'test_out.dat')

with open('test_out.dat', 'rb') as f:
    print(f.read())
'''

#
# Foutsituaties
#
'''
with open('data.txt', 'w') as f:
    for i in range(4):
        f.write(f'{i}\n')

lst = [0, 0, 0, 0]
try:
    with open('data.txt', 'r') as f:
        count = 0
        for line in f.readlines():
            lst[count] = int(line)
            count += 1
except FileNotFoundError as e1:
    print(e1)
except IndexError as e2:
    print(e2)
except ValueError as e3:
    print(e3)
'''  

#
# Weekdagen
#
'''
def tekst_dag(dagnum):
	dagen = ("Zondag", "Maandag", "Dinsdag", "Woensdag", "Donderdag", \
	    "Vrijdag", "Zaterdag")
	try:
		return dagen[dagnum]
	except IndexError as e:
		print('Dagnummer moet tussen 0 en 6 liggen')
		raise e
print(tekst_dag(3))
print(tekst_dag(7))
'''

#
# turtle graphics
#
'''
import turtle

# triangle
turtle.penup()
turtle.setposition(-100, -100)
turtle.pendown()
turtle.left(45)
turtle.forward(141)
turtle.right(90)
turtle.forward(141)
turtle.right(135)
turtle.forward(200)

# circle
turtle.penup()
turtle.setposition(200, 200)
turtle.pendown()
turtle.circle(100)

import math

# spiral
turtle.penup()
turtle.setposition(0, 0)
turtle.pendown()

angle = 0.0
radius = 0.0
delta_angle = 5

while radius < 300:
    x = math.sin(angle * math.pi / 180.0) * radius
    y = math.cos(angle * math.pi / 180.0) * radius
    
    turtle.setposition(x,y)
    
    angle += delta_angle
    if angle > 360.0:
        angle -= 360.0
    radius += 0.2

turtle.done()
'''
