######################################################################
#
#    Simple Trigonometric Graphing Calculator
#    
#    Christopher Henderson
#    
#    This work is licensed under a Creative Commons Attribution 3.0 Unported License.
#    https://creativecommons.org/licenses/by/3.0/deed.en_US
#
######################################################################

import turtle
from sys import exit
from math import sin
from math import cos
from math import tan
from math import pi
from math import fabs

def functionChoser():
    
    while True:
        try:
            userInput = int(raw_input('\n1=sin 2=cos 3=tan \n4=csc 5=sec 6=cot '))
        except ValueError:
            print 'Please enter a number to select your trigonometric function.'
            continue
    
        if userInput in range(1,7):
            return userInput
        else:
            print '\nPlease enter either 1, 2 or 3.'
            continue

def constantsInput():
    global A
    global B
    global C
    global D
    
    A = input('\nA = ')
    B = input('B = ')
    C = input('C = ')
    D = input('D = ')

def operationChooser(constant):
    if constant >= 0:
        return '+'
    else:
        return '-'
    
def exitContinue():
    while True:
        regraph = raw_input('Make another graph? ')
        if regraph == "No" or regraph == "no" or regraph == "N" or regraph == "n":
            exit()
        elif regraph == "Yes" or regraph == "yes" or regraph == "Y" or regraph == "y":
            break

#<---------------Create Window and Initialize Variables-------------------->#
wn = turtle.Screen()
wn.setworldcoordinates(-2,-25,26*pi,25)
graph = turtle.Turtle()
graph.speed(0)
graph.left(90)
graph.forward(23)
graph.stamp()
graph.penup()
graph.goto(0,0)
graph.right(90)
graph.pendown()
graph.forward(26*pi)
graph.stamp()
graph.penup()
graph.goto(0,0)
graph.right(90)
graph.pendown()
graph.forward(23)
graph.stamp()
graph.left(90)
graph.hideturtle()
graph.penup()

for i in range(2,26,2):
    graph.goto(i*pi, -1.5)
    graph.write(str(i)+'pi',align="center")
    graph.goto(i*pi,0)
    graph.pendown()
    graph.left(90)
    graph.forward(.5)
    graph.right(180)
    graph.forward(1)
    graph.left(90)
    graph.penup()
    
for i in range (-20,25,5):
    graph.goto(-2,i)
    graph.write(i,align="center")
    graph.goto(0,i)
    graph.pendown()
    graph.forward(.5)
    graph.backward(1)
    graph.penup()
    
A = 0
B = 0
x = 0
C = 0
D = 0

#<---------------Create Graphing Object-------------------->#
wave = turtle.Turtle()
wave.hideturtle()
wave.speed(0)

#<---------------Graph Loop-------------------->#

print ('\nAll values must be entered as a decimal, integer or a fully qualified operation (e.g. pi/2 or 2*pi.)')
print ('Please consider using floating point operations in place of integer operations (e.g 1.0/2.0 in place of 1/2).\n1/2 will perform integer math, resulting in 0 instead of 0.5.\n')

while True:

    wave.clear()
    wave.penup()
    wave.goto(0,0)
    wave.pendown()
    x = 0
    function = functionChoser()
    
    if function == 1:
        constantsInput()
        print '\nGraphing: '+str(A)+'sin('+str(B)+'(x '+operationChooser(C),str(fabs(C))+'))',operationChooser(D),str(fabs(D))+'\n'
        while x <= 26*pi:
            y = A*sin(B*(x+C))+D
            wave.goto(x,y)
            x += .1
    
    elif function == 2:
        constantsInput()
        print '\nGraphing: '+str(A)+'cos('+str(B)+'(x '+operationChooser(C),str(fabs(C))+'))',operationChooser(D),str(fabs(D))+'\n'
        while x <= 26*pi:
            y = A*cos(B*(x+C))+D
            wave.goto(x,y)
            x += .1
    
    elif function == 3:
        constantsInput()
        print '\nGraphing: '+str(A)+'tan('+str(B)+'(x '+operationChooser(C),str(fabs(C))+'))',operationChooser(D),str(fabs(D))+'\n'
        while x <= 26*pi:
            y = A*tan(B*(x+C))+D
            wave.goto(x,y)
            x += .1
    
    elif function == 4:
        constantsInput()
        print '\nGraphing: '+str(A)+'csc('+str(B)+'(x '+operationChooser(C),str(fabs(C))+'))',operationChooser(D),str(fabs(D))+'\n'
        while x <= 26*pi:
            try:
                y = A*(1/(sin(B*(x+C))))+D
                wave.goto(x,y)
                x += .1
            except ZeroDivisionError:
                x += .1

    elif function == 5:
        constantsInput()
        print '\nGraphing: '+str(A)+'sec('+str(B)+'(x '+operationChooser(C),str(fabs(C))+'))',operationChooser(D),str(fabs(D))+'\n'
        while x <= 26*pi:
            try:
                y = A*(1/(cos(B*(x+C))))+D
                wave.goto(x,y)
                x += .1
            except ZeroDivisionError:
                x += .1

    elif function == 6:
        constantsInput()
        print '\nGraphing: '+str(A)+'cot('+str(B)+'(x '+operationChooser(C),str(fabs(C))+'))',operationChooser(D),str(fabs(D))+'\n'
        while x <= 26*pi:
            try:
                y = A*(1/(tan(B*(x+C))))+D
                wave.goto(x,y)
                x += .1
            except ZeroDivisionError:
                x += .1
                
    exitContinue()
