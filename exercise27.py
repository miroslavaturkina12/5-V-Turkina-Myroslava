from turtle import *

n = int(input('Введіть кількість кутів: '))

if n == 3:
    forward(50)
    right(120)
    forward(50)
    right(120)
    forward(50)
    right(120)

if n == 4:
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    
if n == 5:
    forward(50)
    right(72)
    forward(50)
    right(72)
    forward(50)
    right(72)
    forward(50)
    right(72)
    forward(50)
    right(72)

if n < 3 or n > 5:
    print('Такої фігури не передбачено')

done()