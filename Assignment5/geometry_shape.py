import turtle

SQUARE = "1"
CIRCLE = "2"
TRIANGLE = "3"
QUIT = "4"

def main():
    #TODO: reference lecture5 slide#65 to call the function to draw the requested shape until user chooses to quit
    display_menu()
    CHOICE = int(input("Enter your choice: "))

    while CHOICE != 4:
        if CHOICE == 1:
            square(0, 0, 100, "blue")
        elif CHOICE == 2:
            circle(0, 0, 50, "red")
        elif CHOICE == 3:
            equilateral_triangle(0, 0, 100, "green")
        display_menu()
        CHOICE = int(input("Enter your choice: "))

    turtle.done()

def display_menu():
    print()
    print("Shape Menu")
    print("1) Draw a Square")
    print("2) Draw a Circle")
    print("3) Draw an Equilateral Triangle")
    print("4) Quit")

#TODO: copy the code from lecture5 slide# 69
def square(x, y, side, color):
    turtle.penup()              
    turtle.goto(x, y)           
    turtle.fillcolor(color)     
    turtle.pendown()            
    turtle.begin_fill()         
    for count in range(4):      
        turtle.forward(side)
        turtle.left(90)
    turtle.end_fill()
    pass
   

def equilateral_triangle(x, y, side, color):
    # draw a triangle starting coordinate at x,y
    turtle.penup()              
    turtle.goto(x, y)           
    turtle.fillcolor(color)     
    turtle.pendown()            
    turtle.begin_fill()         
    for count in range(3):      
        turtle.forward(side)
        turtle.left(120)
    turtle.end_fill()

#TODO: copy lecture slide 71 code
def circle(x, y, radius, color):
    turtle.penup()              
    turtle.goto(x, y - radius)  
    turtle.fillcolor(color)     
    turtle.pendown()            
    turtle.begin_fill()         
    turtle.circle(radius)       
    turtle.end_fill()
    pass

if __name__ == "__main__":
    main()