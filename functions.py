import turtle

sufi_turtle = turtle.Turtle()


# Square
def square():
    sufi_turtle.forward(100)
    sufi_turtle.right(90)
    sufi_turtle.forward(100)
    sufi_turtle.right(90)
    sufi_turtle.forward(100)
    sufi_turtle.right(90)
    sufi_turtle.forward(100)


square()
sufi_turtle.forward(300)
square()

turtle.done()