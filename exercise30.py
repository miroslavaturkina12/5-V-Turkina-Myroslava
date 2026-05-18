from turtle  import *
from random  import *

setup (400,400)
bgcolor ('darkblue')
colors  = ['white', 'yellow', 'orange' ]
speed(0)

for i in  range(1,100):
  color (colors [i % 3])
  up()
  goto(randint(-200,200), randint(1,8))

end_fill()