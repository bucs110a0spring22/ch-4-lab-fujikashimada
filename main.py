import math
import turtle

########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help
def drawSineCurve(turtle=None):
  for x_value in range(720):
    y_value = math.sin(math.radians(x_value-360))
    turtle.goto(x_value-360, y_value)
    turtle.down()
  turtle.up()

def drawCosineCurve(turtle=None):
  for x_value in range(720):
    y_value = math.cos(math.radians(x_value-360))
    turtle.goto(x_value-360, y_value) 
    turtle.down()
  turtle.up()

def drawTangentCurve(turtle=None):
  for x_value in range(720):
    if (x_value % 90 != 0):
      y_value = math.tan(math.radians(x_value-360))
      turtle.goto(x_value-360, y_value)
      turtle.down()
    else:
      turtle.up()
  turtle.up()

def setupWindow(wn=None):
  wn.setworldcoordinates(-360, -2, 360, 2)

def setupAxis(turtle=None):
  turtle.goto(0, -2)
  turtle.down()
  turtle.goto(0, 2)
  turtle.up()
  turtle.goto(360, 0)
  turtle.down()
  turtle.goto(-360, 0)
  turtle.up()

##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
