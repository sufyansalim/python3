import turtle

sufi_turtle = turtle.Turtle()
sufi_turtle.speed(15)


# Square
def square():
    sufi_turtle.forward(100)
    sufi_turtle.right(90)
    sufi_turtle.forward(100)
    sufi_turtle.right(90)
    sufi_turtle.forward(100)
    sufi_turtle.right(90)
    sufi_turtle.forward(100)

elephant_weight = 3000
ant_weight = 0.1

# if elephant_weight < ant_weight:
#     square()
# else:
#     sufi_turtle.forward(100)


# sufi = "happy"
# while sufi == "happy":
#     sufi_turtle.forward(10)

for i in range(4):
    square()

turtle.done()