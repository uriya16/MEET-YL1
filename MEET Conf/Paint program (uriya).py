import turtle

turtle.hideturtle()
turtle.speed(0)

color = "white"
shape = "square"
size = 30

def box(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x,y+50)
    turtle.goto(x+50,y+50)
    turtle.goto(x+50,y)
    turtle.goto(x,y)
    turtle.penup()

def color_box(x,y,color):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.goto(x,y+50)
    turtle.goto(x+50,y+50)
    turtle.goto(x+50,y)
    turtle.goto(x,y)
    turtle.end_fill()
    turtle.penup()
    
def triangle(x,y,size,color):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.goto(x+size/2,y+size)
    turtle.goto(x+size,y)
    turtle.goto(x,y)
    turtle.end_fill()
    turtle.penup()

def circle(x,y,size,color):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(size/2)
    turtle.end_fill()
    turtle.penup()

def square(x,y,size,color):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.goto(x+size,y)
    turtle.goto(x+size,y+size)
    turtle.goto(x,y+size)
    turtle.goto(x,y)
    turtle.end_fill()
    turtle.penup()

def plus(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x+30,y)
    turtle.penup()
    turtle.goto(x+15,y-15)
    turtle.pendown()
    turtle.goto(x+15,y+15)
    turtle.penup()

def minus(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x+30,y)
    turtle.penup()

def click_action(x,y):
    if ((x > -140 and x < -90) and (y>190 and y<240)):
        global shape
        shape = "square"
    if ((x > -90 and x < -40) and (y>190 and y<240)):
        global shape
        shape = "circle"
    if ((x > -40 and x < 10) and (y>190 and y<240)):
        global shape
        shape = "triangle"
    if ((x > 10 and x < 60) and (y>190 and y<240)):
        global size
        size = size + 5
    if ((x > 60 and x < 110) and (y>190 and y<240)):
        global size
        size = size - 5
    if ((x > 250 and x < 300) and (y>100 and y<150)):
        global color
        color = "blue"
    if ((x > 250 and x < 300) and (y>50 and y<100)):
        global color
        color = "green"
    if ((x > 250 and x < 300) and (y>0 and y<50)):
        global color
        color = "red"
    if ((x > 250 and x < 300) and (y>-50 and y<0)):
        global color
        color = "yellow"


def draw_shape(x,y):
    if shape == "square":
        square(x,y,size,color)
    if shape == "triangle":
        triangle(x,y,size,color)
    if shape == "circle":
        circle(x,y,size,color)
    

square(-130,200,30,color)
circle(-65,200,30,color)
triangle(-30,200,30,color)
plus(20,215)
minus(70,215)
box(-140,190)
box(-90,190)
box(-40,190)
box(10,190)
box(60,190)
color_box(250,100, "blue")
color_box(250,50,"green")
color_box(250,0, "red")
color_box(250,-50, "yellow")

turtle.onscreenclick ( click_action ,  btn=3 ,  add = True )
turtle.onscreenclick ( draw_shape ,  btn=1 ,  add = True )
turtle.getscreen().listen()
turtle.mainloop()
