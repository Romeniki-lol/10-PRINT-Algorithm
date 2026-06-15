import tkinter as tk
from tkinter import *
import random

height = 1000
width = 1000
cell_size = 50

root = tk.Tk()
root.title("Maze Ig")

canvas = Canvas(root, width=width, height=height,bg="black")
canvas.pack()

def GenerateMaze():
    for x in range(0, width, cell_size):
        for y in range(0, height, cell_size):
            coin = random.choice([True, False])
            if coin == True:
                canvas.create_line(x,y,x+cell_size,y+cell_size, fill="#ff0000", width=4)
            else:
                canvas.create_line(x, y+cell_size, x+cell_size,y, fill="#ff0000", width=4)

GenerateMaze()

root.mainloop()
