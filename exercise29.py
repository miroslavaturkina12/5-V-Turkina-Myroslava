from turtle  import *
color ('blue')
speed(0)
for i in range(1,100,2):
   up()
   goto (i*2,i*1.5)
   down()
   circle (i)

done()