import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("pink")
drawing_board.title("Python  Turtle")

shrinking_square = turtle.Turtle()
b = 200

while b > 0:
    b = b - 4
    shrinking_square.forward(b)
    shrinking_square.left(90)

turtle.done()