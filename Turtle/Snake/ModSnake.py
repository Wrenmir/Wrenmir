#---import section
import turtle as t
#from turtle import *
import random as r
import time

#---global var or objects or game config
delay=0.1
bodyPartsPlayer1=[]        #bodyPart(s) plural so should be a list
bodyPartsPlayer2=[]

wn=t.Screen()
wn.title("Multiplayer Snake Game")
wn.setup(width=600,height=600)  #each time the game turns on, sets the w,h
wn.bgcolor("gray")

#Main Menu Mods - CREDIT TO DOM
main_menu = t.Turtle()  #creating a turtle to display the main menu
main_menu.speed(0)
main_menu.color("white")
main_menu.penup()
main_menu.hideturtle()
main_menu.goto(0,50)
main_menu.write("Snake Game", align = "center", font = ("Courier", 24, "normal")) #writing the title
main_menu.goto(0,0)
#option for pvc
main_menu.write("Press '1' for PVC", align="center", font=("Courier", 16, "normal"))
main_menu.goto(0, -50)
#option for pvp
main_menu.write("Press '2' for PVP", align="center", font=("Courier", 16, "normal"))

#Player 1
headPlayer1 = t.Turtle(shape="square")
headPlayer1.speed(0)
headPlayer1.penup()
headPlayer1.direction="stop"   #direction the object is pointing; using direction allows you to use the stop command
headPlayer1.color("blue")

#Player 2
headPlayer2 = t.Turtle(shape="square")
headPlayer2.speed(0)
headPlayer2.penup()
headPlayer2.color("purple")
headPlayer2.direction="stop"

food = t.Turtle(shape="circle")
food.speed(0)
food.penup()
food.teleport(100,100)
food.color("red")

#---functions
#move up
def up(player):
    if player.direction != "down":
        player.direction="up"
#move down
def down(player):
    if player.direction != "up":
        player.direction="down"
#move right
def right(player):
    if player.direction != "left":
        player.direction="right"
#move left
def left(player):
    if player.direction != "right":
        player.direction="left"

#movement
def movePlayer(player):
    if player.direction=="up":
        player.sety(player.ycor()+15)
    elif player.direction=="down":
        player.sety(player.ycor()-15)
    elif player.direction=="right":
        player.setx(player.xcor()+15)
    elif player.direction=="left":
        player.setx(player.xcor()-15)

def updateBodyParts(player, bodyParts):
    if len(bodyParts) > 0:
        newX = player.xcor()
        newY = player.ycor()
        tail = bodyParts[-1]
        tail.goto(newX, newY)
        bodyParts.insert(0, tail)
        bodyParts.pop()

#game over function
def hideTheBodyParts(player, bodyParts):
    for eachBodyPart in bodyParts:
            #eachBodyPart.hideturtle()
        eachBodyPart.goto(1000,1000)    #not the best, but it hides the body
    #bodyParts1=[]            #"clearing the list" - reset the list
    bodyParts.clear()
        
#---events 
def PVC():  #CREDIT TO DOM
    global delay
    main_menu.clear()
    headPlayer1.color("red")
    headPlayer2.hideturtle()
    food.color("red")
    bodyPartsPlayer2.clear()
    delay = 0.1
    wn.onkeypress(lambda: up(headPlayer1), "w")
    wn.onkeypress(lambda: down(headPlayer1), "s")
    wn.onkeypress(lambda: left(headPlayer1), "a")
    wn.onkeypress(lambda: right(headPlayer1), "d")
    runGame()

def PVP():  #CREDIT TO DOM
    global delay
    main_menu.clear()
    headPlayer1.color("red")
    headPlayer2.color("blue")
    food.color("red")
    delay = 0.1
    wn.onkeypress(lambda: up(headPlayer1), "w")
    wn.onkeypress(lambda: down(headPlayer1), "s")
    wn.onkeypress(lambda: left(headPlayer1), "a")
    wn.onkeypress(lambda: right(headPlayer1), "d")
    wn.onkeypress(lambda: up(headPlayer2), "Up")
    wn.onkeypress(lambda: down(headPlayer2), "Down")
    wn.onkeypress(lambda: left(headPlayer2), "Left")
    wn.onkeypress(lambda: right(headPlayer2), "Right")
    runGame()

def togglePause():  #CREDIT TO DOM
    global delay
    if delay == 0:
        delay = 0.1
    else:
        delay = 0

# --- key bindings
wn.onkeypress(PVC, "1")
wn.onkeypress(PVP, "2")

#---main loop
def runGame(): 
    global delay
    while True:        #runs the code over and over
        wn.update()     #update or refresh the screen
        #Check for wall collision
        #if head.collideWith(wall):
            #head.teleport(0,0)
                #up               #down             #right              #left
        if headPlayer1.ycor()>290 or headPlayer1.ycor()<-290 or headPlayer1.xcor()>290 or headPlayer1.xcor()<-290:
            hideTheBodyParts(headPlayer1,bodyPartsPlayer1) 
        if (headPlayer2.ycor() > 290 or headPlayer2.ycor() < -290 or headPlayer2.xcor() < -290 or headPlayer2.xcor() > 290):
            hideTheBodyParts(headPlayer2, bodyPartsPlayer2)
        #Check for food collision
        #  distace btwn head and food
        if headPlayer1.distance(food) < 20:
            food.teleport(r.randint(-270,270),r.randint(-270,270))
            bodyPart = t.Turtle(shape="square")
            bodyPart.speed(0)
            bodyPart.penup()
            bodyPart.color("red")
            bodyPartsPlayer1.append(bodyPart)
        if headPlayer2.distance(food) < 20:
            food.teleport(r.randint(-270,270),r.randint(-270,270))
            bodyPart = t.Turtle(shape="square")
            bodyPart.speed(0)
            bodyPart.penup()
            bodyPart.color("blue")
            bodyPartsPlayer2.append(bodyPart)

        #Move the body parts ; follow the leader
        #move the butt to the neck
        #        range(tailIndex,neckIndex,stepBy -1)
        for i in range(len(bodyPartsPlayer1)-1,0,-1):
            newX=bodyPartsPlayer1[i-1].xcor()
            newY=bodyPartsPlayer1[i-1].ycor()
            bodyPartsPlayer1[i].goto(newX,newY)
        for i in range(len(bodyPartsPlayer2)-1,0,-1):
            newX=bodyPartsPlayer2[i-1].xcor()
            newY=bodyPartsPlayer2[i-1].ycor()
            bodyPartsPlayer2[i].goto(newX,newY)

        #Move the neck to the head
        if len(bodyPartsPlayer1)>0:        #only runs when there are bodyParts
            newX=headPlayer1.xcor()
            newY=headPlayer1.ycor()
            neck1=bodyPartsPlayer1[0]
            neck1.goto(newX,newY)
        if len(bodyPartsPlayer2)>0:        #only runs when there are bodyParts
            newX=headPlayer2.xcor()
            newY=headPlayer2.ycor()
            neck2=bodyPartsPlayer2[0]
            neck2.goto(newX,newY)

        #Move the head forward
        movePlayer(headPlayer1)
        movePlayer(headPlayer2)

        #Check for individual body collision
        #if any of the bodyParts are within some value of another bodyPart
        for eachBodyPart in bodyPartsPlayer1:
            if headPlayer1.distance(eachBodyPart)<10:
                hideTheBodyParts(headPlayer1,bodyPartsPlayer1)
        for eachBodyPart in bodyPartsPlayer2:
            if headPlayer2.distance(eachBodyPart)<10:
                hideTheBodyParts(headPlayer2,bodyPartsPlayer2)

        #Speed up as you eat food mod - CRED TO DOM
        delay -= 0.005

        #Non-negative delay
        if delay <= 0:
            delay = 0.1     #Set to a default pos value

        #Hard mode mod - CRED TO DOM
            if int(time.time()) % 10 == 0: #every ten seconds
                food.goto(r.randint(-290, 290), r.randint(-290, 290)) #teleport food
        
wn.listen()
wn.mainloop()
#time.sleep(delay)   #time module tells the program to sleep by some delay