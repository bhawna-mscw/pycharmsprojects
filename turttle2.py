"""
Let the user specify how many sides the object will have and draw whatever they ask
"""
import turtle
num=int(input("Enter the number of sides: "))
for i in range(num):
    turtle.forward(100)
    turtle.right(45)