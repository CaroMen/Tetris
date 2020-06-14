# Instagram: @carocode_
# Following a tutorial to get a better understanding of thought process behind
# building a project to later rebuild something myself

import turtle
import time
import random

# Screen Info
screen = turtle.Screen()
screen.title("Tetris by @CaroCode_")
screen.bgcolor("black")
screen.setup(width=600, height=800)
screen.tracer(0)

delay = 0.05

# Shapes


class shapes():
    def __init__(self):
        self.x = 5
        self.y = 0
        self.color = random.randint(1, 7)

    def left_move(self, grid):
        if self.x > 0:
            if grid[self.y][self.x - 1] == 0:
                grid[self.y][self.x] = 0
                self.x -= 1

    def right_move(self, grid):
        if self.x < 11:  # keeps it from going off grid
            if grid[self.y][self.x + 1] == 0:  # checks to see if there's something in the way
                grid[self.y][self.x] = 0
                self.x += 1


# List to store column and row information
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4]
]

# Turtle drawing
pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.shape("square")
pen.setundobuffer(None)


def create_grid(pen, grid):
    pen.clear()  # clears everything off the screen
    top = 230
    left = -110

    # Colors
    colors = ["black", "red", "lightblue", "orange",
              "blue", "yellow", "green", "purple"]

    for y in range(len(grid)):
        for x in range(len(grid[0])):  # starting at index 0
            scr_x = left + (x * 20)  # starts the object away from the edge
            scr_y = top - (y * 20)  # moves down vertically?
            color_num = grid[y][x]
            color = colors[color_num]
            pen.color(color)  # changes color from black
            pen.goto(scr_x, scr_y)
            pen.stamp()


def check_grid(grid):
    # check if each row is full
    y = 23
    while y > 0:
        is_full = True
        for x in range(0, 12):
            if grid[y][x] == 0:
                is_full = False
                y -= 1
                break

        if is_full:
            global score
            score += 10
            draw_score(pen, score)
            for copy_y in range(22, 0, -1):
                for copy_x in range(0, 12):
                    grid[copy_y + 1][copy_x] = grid[copy_y][copy_x]


def draw_score(pen, score):
    pen.hideturtle()
    pen.goto(-75, 350)
    pen.write("Score: {}".format(score), move=False,
              align="left", font=("Arial", 24, "normal"))
    pen.showturtle()


# creates shapes
shape = shapes()

# puts shapes in grid
grid[shape.y][shape.x] = shape.color

# Draw grid
#create_grid(pen, grid)

# Move left and right
screen.listen()
screen.onkeypress(lambda: shape.left_move(grid), "a")
screen.onkeypress(lambda: shape.right_move(grid), "d")

# Set score to zero
score = 0
draw_score(pen, score)

# Main game
while True:
    screen.update()
    # Move the shape
    # Open row
    if shape.y == 23:  # if at bottom row
        shape = shapes()  # make a new shape
        check_grid(grid)
    elif grid[shape.y + 1][shape.x] == 0:  # if space below, move
        grid[shape.y][shape.x] = 0  # sets the previous index back to zero
        shape.y += 1  # goes to the next index
        grid[shape.y][shape.x] = shape.color  # gives the color
    else:
        shape = shapes()  # else, make a new shape
        check_grid(grid)

    # draw screen
    draw_score(pen, score)
    create_grid(pen, grid)

    time.sleep(delay)

# Keep window open
screen.mainloop()
