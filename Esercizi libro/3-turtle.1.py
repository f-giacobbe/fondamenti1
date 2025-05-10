import turtle
import time

window_color = input("Select the background color: ")
ciccio_color = input("Select Ciccio's color: ")

window = turtle.Screen()
window.bgcolor(window_color)    #window background color
window.title("Hello, Ciccio")   #window title

ciccio = turtle.Turtle()
ciccio.color(ciccio_color)
ciccio.pensize(3)   #line thickness

ciccio.forward(50)
time.sleep(1)
ciccio.left(120)
time.sleep(1)
ciccio.forward(50)

window.mainloop()