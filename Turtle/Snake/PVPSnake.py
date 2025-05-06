#---import section
import turtle as t
#from turtle import *
import random as r
import time

#---global var or objects or game config
delay=0.1
bodyParts1=[]        #bodyPart(s) plural so should be a list
bodyParts2=[]

wn=t.Screen()
wn.setup(width=600,height=600)  #each time the game turns on, sets the w,h
wn.bgcolor("gray")

head1 = t.Turtle(shape="square")
head1.speed(0)
head1.penup()
head1.direction="stop"   #direction the object is pointing; using direction allows you to use the stop command
head1.color("blue")
head1.teleport(-20,0)

head2 = t.Turtle(shape="square")
head2.speed(0)
head2.penup()
head2.color("purple")
head2.direction="stop"
head2.teleport(20,0)

food = t.Turtle(shape="circle")
food.speed(0)
food.penup()
food.teleport(100,100)
food.color("red")

#---functions
#move up
def up1():
    if head1.direction != "down":
        head1.direction="up"
def up2():
    if head2.direction != "down":
        head2.direction="up"
#move down
def down1():
    if head1.direction != "up":
        head1.direction="down"
def down2():
    if head2.direction != "up":
        head2.direction="down"
#move right
def right1():
    if head1.direction != "left":
        head1.direction="right"
def right2():
    if head2.direction != "left":
        head2.direction="right"
#move left
def left1():
    if head1.direction != "right":
        head1.direction="left"
def left2():
    if head2.direction != "right":
        head2.direction="left"

#movement
def move1():
    if head1.direction=="up":
        head1.sety(head1.ycor()+15)
    elif head1.direction=="down":
        head1.sety(head1.ycor()-15)
    elif head1.direction=="right":
        head1.setx(head1.xcor()+15)
    elif head1.direction=="left":
        head1.setx(head1.xcor()-15)
def move2():
    if head2.direction=="up":
        head2.sety(head2.ycor()+15)
    elif head2.direction=="down":
        head2.sety(head2.ycor()-15)
    elif head2.direction=="right":
        head2.setx(head2.xcor()+15)
    elif head2.direction=="left":
        head2.setx(head2.xcor()-15)

#game over function
def hideTheBodyParts1():
    global bodyParts1        #this tells py that bodyParts is a global var
    head1.teleport(0,0)
    for eachBodyPart1 in bodyParts1:
            #eachBodyPart.hideturtle()
        eachBodyPart1.goto(610,610)    #not the best, but it hides the body
    bodyParts1=[]            #"clearing the list" - reset the list
def hideTheBodyParts2():
    global bodyParts2        #this tells py that bodyParts is a global var
    head2.teleport(0,0)
    for eachBodyPart2 in bodyParts2:
            #eachBodyPart.hideturtle()
        eachBodyPart2.goto(610,610)    #not the best, but it hides the body
    bodyParts2=[]  

#---events
#window.onkeypress(command,"keyboard character")
wn.onkeypress(up1,"w")   #keyboard bindings from the window object
wn.onkeypress(down1,"s")
wn.onkeypress(right1,"d")
wn.onkeypress(left1,"a")
wn.onkeypress(up2,"Up")   #keyboard bindings from the window object
wn.onkeypress(down2,"Down")
wn.onkeypress(right2,"Right")
wn.onkeypress(left2,"Left")
wn.listen()             #tells the window to listen for key presses

#---main loop
while True:         #runs the code over and over
    wn.update()     #update or refresh the screen
    #Check for wall collision
    #if head.collideWith(wall):
        #head.teleport(0,0)
            #up               #down             #right              #left
    if head1.ycor()>290 or head1.ycor()<-290 or head1.xcor()>290 or head1.xcor()<-290:
        hideTheBodyParts1()
    if head2.ycor()>290 or head2.ycor()<-290 or head2.xcor()>290 or head2.xcor()<-290:
        hideTheBodyParts2()    
    #Check for food collision
    #  distace btwn head and food
    if head1.distance(food) < 20:
        food.teleport(r.randint(-270,270),r.randint(-270,270))
        bodyPart1 = t.Turtle(shape="square")
        bodyPart1.speed(0)
        bodyPart1.penup()
        bodyParts1.append(bodyPart1)
        print(bodyParts1)
    if head2.distance(food) < 20:
        food.teleport(r.randint(-270,270),r.randint(-270,270))
        bodyPart2 = t.Turtle(shape="square")
        bodyPart2.speed(0)
        bodyPart2.penup()
        bodyParts2.append(bodyPart2)
        print(bodyParts2)
    for TheBodyParts1 in bodyParts1:
        TheBodyParts1.color("blue")
    for TheBodyParts2 in bodyParts2:
        TheBodyParts2.color("purple")

    #Move the body parts ; follow the leader
    #move the butt to the neck
    #        range(tailIndex,neckIndex,stepBy -1)
    for i in range(len(bodyParts1)-1,0,-1):
        newX=bodyParts1[i-1].xcor()
        newY=bodyParts1[i-1].ycor()
        bodyParts1[i].goto(newX,newY)
    for i in range(len(bodyParts2)-1,0,-1):
        newX=bodyParts2[i-1].xcor()
        newY=bodyParts2[i-1].ycor()
        bodyParts2[i].goto(newX,newY)

    #Move the neck to the head
    if len(bodyParts1)>0:        #only runs when there are bodyParts
        newX=head1.xcor()
        newY=head1.ycor()
        neck1=bodyParts1[0]
        neck1.goto(newX,newY)
    if len(bodyParts2)>0:        #only runs when there are bodyParts
        newX=head2.xcor()
        newY=head2.ycor()
        neck2=bodyParts2[0]
        neck2.goto(newX,newY)

    #Move the head forward
    move1()
    move2()

    #Check for individual body collision
    #if any of the bodyParts are within some value of another bodyPart
    for eachBodyPart1 in bodyParts1:
        if head1.distance(eachBodyPart1)<10:
            hideTheBodyParts1()
    for eachBodyPart2 in bodyParts2:
        if head2.distance(eachBodyPart2)<10:
            hideTheBodyParts2()
    #Check for collision between snakes
    for eachBodyPart2 in bodyParts2:
        if head1.distance(eachBodyPart2)<10:
            hideTheBodyParts1()
    for eachBodyPart1 in bodyParts1:
        if head2.distance(eachBodyPart1)<10:
            hideTheBodyParts2()

    time.sleep(delay)   #time module tells the program to sleep by some delay