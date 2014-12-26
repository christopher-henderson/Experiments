###########################################################################################
#
#    Christopher Henderson
#    October XXnd, 2013   
#    CST 100 - TTh - Prof. Richard Whitehouse
#
#
#    Lab 3 - Fall 2013
#    angry_projectiles.py
#
###########################################################################################

import turtle
import math
import random
from sys import exit
from sys import version_info

def plusVelocity():
    global velocity
    if velocity < 999:
        velocity += 1
        textVelocity.clear()
        textVelocity.write(velocity, align='center')
    
def minusVelocity():
    global velocity
    if velocity > 1:
        velocity -= 1
        textVelocity.clear()
        textVelocity.write(velocity, align='center')

def plusAngle():
    global angle
    if angle < 90:
        angle += 1
        textAngle.clear()
        textAngle.write(angle, align='center')
        angry.settiltangle(angle)

def minusAngle():
    global angle
    if angle > 1:
        angle -= 1
        textAngle.clear()
        textAngle.write(angle, align='center')
        angry.settiltangle(angle)
        
def clearScreen():
    angry.clear()

def exitGame():
    if versionCheck() == True:
        unbindEventsPython3()
    else:
        unbindEventsPython2()
    
    wn.delay(1)
    wn.reset()

    for turtles in wn.turtles():
        turtles.hideturtle()
        
    exitSplash = turtle.Turtle()
    exitSplash.penup()
    exitSplash.hideturtle()
    exitSplash.speed(0)
    exitSplash.setposition(200, 150)
    exitSplash.write('Thank you for playing...', align='center')
    exitSplash.setposition(200, 130)
    exitSplash.write('Angry Projectiles!', align='center',font=('', 32, "italic"))
    exitSplash.setposition(200, 120)
    exitSplash.write('Check out our new game, Angry Projectiles in Space!, on April 1, 20XX.', align='center')
    wn.ontimer(exit,5000)

def trajectory():
    if versionCheck() == True:
        unbindEventsPython3()
    else:
        unbindEventsPython2()
    
    angleRadians = math.radians(angle)
    increment = 1
    distance = increment
    gravity = 32.17
    height = 1

    while height > 0:
        time = distance / (velocity * math.cos(angleRadians))
        height = velocity * time * math.sin(angleRadians) - gravity * math.pow(time,2) / 2
        
        if height >= 0:
            angry.settiltangle(angry.towards(distance,height))      #
            angry.goto(distance,height)                             #    This block prevents the angry
            distance += increment                                   #    projectile from going under the x-axis
        else:                                                       #    and informs the user when they've
            angry.goto(distance,0)                                  #    overshot the map
                                                                    #

        if distance >= targetLocation and distance <= targetLocation + 10 and height >= 0 and height <= 30:     # Did we hit the target?
            angry.goto(distance,height)
            messenger.write('Now you\'re wanted for murder!', align='center',font=('', 32, "italic"))
            wn.ontimer(messenger.clear,2000)
            break

        if distance >= 400:                                          
            messenger.write('You overshot the map!', align='center',font=('', 32, "italic"))
            wn.ontimer(messenger.clear,2000)
            break

    angry.stamp()
    angry.hideturtle()
    angry.penup()
    angry.setposition(0,0)
    angry.settiltangle(angle)
    angry.showturtle()
    angry.pendown()
    
    if versionCheck() == True:
        bindEventsPython3()
    else:
        bindEventsPython2()

#------- From here on we have to provide compatiblity for both Python 3.x and Python 2.x

def versionCheck():
    if version_info[0] >= 3:
        return True
    else:
        return False

#------- Python 3
def bindEventsPython3():
    wn.onkey(clearScreen,"Delete")
    wn.onkey(clearScreen,"BackSpace")
    wn.onkey(exitGame,"Escape")
    wn.onkey(exitGame,"q")
    wn.onkey(trajectory, "space")
    
    wn.onkeypress(plusVelocity, "Right")
    wn.onkeypress(minusVelocity, "Left")
    wn.onkeypress(plusAngle, "Up")
    wn.onkeypress(minusAngle, "Down")
    
def unbindEventsPython3():
    wn.onkey(None,"Delete")
    wn.onkey(None,"BackSpace")
    wn.onkey(None,"Escape")
    wn.onkey(None,"q")
    wn.onkey(None, "space")
    
    wn.onkeypress(None, "Right")
    wn.onkeypress(None, "Left")
    wn.onkeypress(None, "Up")
    wn.onkeypress(None, "Down")
    
#------- Python 2
def bindEventsPython2():
    wn.onkey(clearScreen,"Delete")
    wn.onkey(clearScreen,"BackSpace")
    wn.onkey(exitGame,"Escape")
    wn.onkey(exitGame,"q")
    wn.onkey(trajectory, "space")

    wn.onkey(plusVelocity, "Right")
    wn.onkey(minusVelocity, "Left")
    wn.onkey(plusAngle, "Up")
    wn.onkey(minusAngle, "Down")
        
def unbindEventsPython2():
    wn.onkey(None,"Delete")
    wn.onkey(None,"BackSpace")
    wn.onkey(None,"Escape")
    wn.onkey(None,"q")
    wn.onkey(None, "space")

    wn.onkey(None, "Right")
    wn.onkey(None, "Left")
    wn.onkey(None, "Up")
    wn.onkey(None, "Down")





























#------- Setup an appropriately sized screen and draw our killing field.

wn = turtle.Screen()
wn.delay(1)
wn.setworldcoordinates(-5,-5,405,205)
wn.title('Welcome to Angry Projectiles!')
graph = turtle.Turtle()
graph.speed(0)
graph.left(90)
graph.forward(200)
graph.stamp()
graph.penup()
graph.goto(0,0)
graph.right(90)
graph.pendown()
graph.forward(400)
graph.stamp()

targetLocation = random.randint(100,301)
target = turtle.Turtle()
target.penup()
target.hideturtle()
target.goto(targetLocation,0)
target.pendown()
target.left(90)
target.forward(30)
target.right(90)
target.forward(10)
target.right(90)
target.forward(30)

#------- Create the turtles that we will be using to report messages and current velocity/angle back to the user.
#------- We need velocity/angle for the text so may as well init those global variables here.
#------- We use multiple, independent, turtles because having one large text field will flash obnoxiously while updating.

velocity = 1
angle = 1

textStatic = turtle.Turtle()
textStatic.speed(0)
textStatic.penup()
textStatic.hideturtle()
textStatic.setposition(75, -5)
textStatic.write ('Velocity:       m/s                     Angle:      degrees', align='center')

textVelocity = turtle.Turtle()
textVelocity.speed(0)
textVelocity.penup()
textVelocity.hideturtle()
textVelocity.setposition(43, -5)
textVelocity.write(velocity, align='center')

textAngle = turtle.Turtle()
textAngle.speed(0)
textAngle.penup()
textAngle.hideturtle()
textAngle.setposition(108, -5)
textAngle.write(angle, align='center')

messenger = turtle.Turtle()
messenger.speed(0)
messenger.hideturtle()
messenger.penup()
messenger.setposition(200,130)

legend = turtle.Turtle()
legend.speed(0)
legend.penup()
legend.hideturtle()
legend.setposition(350,200)
legend.write('Legend', align='center')
legend.setposition(350,198)
legend.write('________________________________', align='center')
legend.setposition(350,194)
legend.write('Angle: Up/Down', align='center')
legend.setposition(350,190)
legend.write('Velocity: Right/Left', align='center')
legend.setposition(350,186)
legend.write('Clear Screen: Delete/Backspace', align='center')
legend.setposition(350,182)
legend.write('Exit Game: Esc/Q', align='center')

#------- When quickly updating text turtle graphics/Tkinter can experience a bug where previous values aren't properly cleared, resulting
#------- in overlapping text. Lowering the screen delay from the default 10 milliseconds to 6 milliseconds seems to fix this.
wn.delay(6)

#------- Beware...I live...
angry = turtle.Turtle()
angry.speed(0)





























#------- "And here...we...go..."
#------- https://www.youtube.com/watch?v=XqwCejSZA28

if versionCheck() == True:
    
    bindEventsPython3()
    wn.listen()
    wn.mainloop()

else:
    
    bindEventsPython2()
    messenger.setposition(200,140)
    messenger.write('You are using Python '+str(version_info[0])+'.'+str(version_info[1])+'.'+str(version_info[2])+'.', align='center')
    messenger.setposition(200,130)
    messenger.write('Loading Python 2 compatiblity...', align='center',font=('', 18, "italic"))
    messenger.setposition(200,120)
    messenger.write('For a more enjoyable experience we suggest using Python 3.', align='center')
    messenger.setposition(200,130)
    wn.ontimer(messenger.clear,8000)
    wn.listen()
    turtle.mainloop()   #<--------- I can't explain why Python 2 doesn't like wn.mainloop(), but it doesn't.