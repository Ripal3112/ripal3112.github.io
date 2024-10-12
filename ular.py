import turtle

def draw_heart():
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(224)
    turtle.circle(-112, 200)
    turtle.left(120)
    turtle.circle(-112, 200)
    turtle.forward(224)
    turtle.end_fill()

def write_name():
    turtle.penup()
    turtle.goto(-80, 95)
    turtle.color("white")
    turtle.pendown()
    turtle.write("Aulia🌷🌸", font=("Arial", 32, "bold"))

turtle.speed(1)
draw_heart()
write_name()
turtle.hideturtle()
turtle.done()
