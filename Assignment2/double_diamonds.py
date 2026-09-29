import turtle

#Drawing right diamond
turtle.fillcolor("red")
turtle.begin_fill()
turtle.left(45)

for i in range(3):
    turtle.forward(100)
    turtle.right(90)

turtle.forward(100)
turtle.end_fill()

#Drawing left diamond
turtle.fillcolor("blue")
turtle.begin_fill()
turtle.left(90)

for i in range(3):
    turtle.forward(100)
    turtle.right(90)

turtle.forward(100)
turtle.end_fill()

turtle.hideturtle()
turtle.done()