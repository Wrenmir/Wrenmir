import turtle as t

wn = t.Screen()
wn.bgcolor("lightGrey")
wn.addshape('leaf.gif')
wn.addshape('star.gif')
wn.addshape('50stars.gif')

#main drawing turtle
mikey = t.Turtle()
mikey.shape('blank')
mikey.speed(20)
mikey.shapesize(1)

#Ghana
    #red stripe
mikey.teleport(-180,120)
mikey.fillcolor("red")
mikey.color("red")
mikey.begin_fill()
for i in range(2):
    mikey.fd(180)
    mikey.rt(90)
    mikey.fd(40)
    mikey.rt(90)
mikey.end_fill()
    #yellow stripe
mikey.teleport(-180,80)
mikey.fillcolor("yellow")
mikey.color("yellow")
mikey.begin_fill()
for i in range(2):
    mikey.fd(180)
    mikey.rt(90)
    mikey.fd(40)
    mikey.rt(90)
mikey.end_fill()
    #green stripe
mikey.teleport(-180,40)
mikey.fillcolor("green")
mikey.color("green")
mikey.begin_fill()
for i in range(2):
    mikey.fd(180)
    mikey.rt(90)
    mikey.fd(40)
    mikey.rt(90)
mikey.end_fill()
    #star
star = t.Turtle()
star.teleport(-90,60)
star.shape('star.gif')

#Finland
    #white background
mikey.teleport(0,120)
mikey.fillcolor("white")
mikey.color("white")
mikey.begin_fill()
for i in range(2):
    mikey.fd(180)
    mikey.rt(90)
    mikey.fd(120)
    mikey.rt(90)
mikey.end_fill()
    #horizontal blue stripe
mikey.teleport(0,75)
mikey.fillcolor("blue")
mikey.color("blue")
mikey.begin_fill()
for i in range(2):
    mikey.fd(180)
    mikey.rt(90)
    mikey.fd(30)
    mikey.rt(90)
mikey.end_fill()
    #vertical blue stripe
mikey.teleport(75,120)
mikey.fillcolor("blue")
mikey.color("blue")
mikey.begin_fill()
mikey.rt(90)
for i in range(2):
    mikey.fd(120)
    mikey.rt(90)
    mikey.fd(30)
    mikey.rt(90)
mikey.end_fill()

#Canada
    #white background
mikey.teleport(-180,0)
mikey.fillcolor("white")
mikey.color("white")
mikey.rt(270)
mikey.begin_fill()
for i in range(2):
    mikey.fd(180)
    mikey.rt(90)
    mikey.fd(120)
    mikey.rt(90)
mikey.end_fill()
    #left red stripe
mikey.teleport(-135,-120)
mikey.fillcolor("red")
mikey.color("red")
mikey.begin_fill()
mikey.rt(180)
for i in range(2):
    mikey.fd(45)
    mikey.rt(90)
    mikey.fd(120)
    mikey.rt(90)
mikey.end_fill()
    #right red stripe
mikey.teleport(0,-120)
mikey.fillcolor("red")
mikey.color("red")
mikey.begin_fill()
for i in range(2):
    mikey.fd(45)
    mikey.rt(90)
    mikey.fd(120)
    mikey.rt(90)
mikey.end_fill()
    #leaf
leaf = t.Turtle()
leaf.teleport(-90,-60)
leaf.shape('leaf.gif')

#Ireland
    #green stripe
mikey.color('green')
mikey.fillcolor('green')
mikey.home()
mikey.begin_fill()
for i in range(2):
    mikey.fd(60)
    mikey.rt(90)
    mikey.fd(120)
    mikey.rt(90)
mikey.end_fill()
    #white stripe
mikey.color('white')
mikey.fillcolor('white')
mikey.teleport(60,0)
mikey.begin_fill()
for i in range(2):
    mikey.fd(60)
    mikey.rt(90)
    mikey.fd(120)
    mikey.rt(90)
mikey.end_fill()
 #orange stripe
mikey.color('orange')
mikey.fillcolor('orange')
mikey.teleport(120,0)
mikey.begin_fill()
for i in range(2):
    mikey.fd(60)
    mikey.rt(90)
    mikey.fd(120)
    mikey.rt(90)
mikey.end_fill()

#Bonus: USA
    #white background
mikey.teleport(-180,-120)
mikey.fillcolor('white')
mikey.color('white')
mikey.begin_fill()
for i in range(2):
    mikey.fd(180)
    mikey.rt(90)
    mikey.fd(120)
    mikey.rt(90)
mikey.end_fill
    #blue box
mikey.teleport(-180,-120)
mikey.color('dark blue')
mikey.fillcolor('dark blue')
mikey.begin_fill
for i in range(2):
    mikey.fd(79)
    mikey.rt(90)
    mikey.fd(63)
    mikey.rt(90)
mikey.end_fill()
    #red stripes
mikey.teleport(-100,-120)
mikey.color('red')
mikey.fillcolor('red')
        #1
mikey.begin_fill()
for i in range(2):
    mikey.fd(100)
    mikey.rt(90)
    mikey.fd(9)
    mikey.rt(90)
mikey.end_fill
        #2
mikey.teleport(-100,-138)
mikey.begin_fill()
for i in range(2):
    mikey.fd(100)
    mikey.rt(90)
    mikey.fd(9)
    mikey.rt(90)
mikey.end_fill
        #3
mikey.teleport(-100,-156)
mikey.begin_fill()
for i in range(2):
    mikey.fd(100)
    mikey.rt(90)
    mikey.fd(9)
    mikey.rt(90)
mikey.end_fill
        #4
mikey.teleport(-100,-174)
mikey.begin_fill()
for i in range(2):
    mikey.fd(100)
    mikey.rt(90)
    mikey.fd(9)
    mikey.rt(90)
mikey.end_fill
        #5
mikey.teleport(-180,-192)
mikey.begin_fill()
for i in range(2):
    mikey.fd(180)
    mikey.rt(90)
    mikey.fd(10)
    mikey.rt(90)
mikey.end_fill
        #6
mikey.teleport(-180,-212)
mikey.begin_fill()
for i in range(2):
    mikey.fd(180)
    mikey.rt(90)
    mikey.fd(10)
    mikey.rt(90)
mikey.end_fill
        #7
mikey.teleport(-180,-230)
mikey.begin_fill()
for i in range(2):
    mikey.fd(180)
    mikey.rt(90)
    mikey.fd(10)
    mikey.rt(90)
mikey.end_fill()
#stars
stars = t.Turtle()
stars.teleport(-140,-151)
stars.shape('50stars.gif')

wn.mainloop()