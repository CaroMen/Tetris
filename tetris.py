# Instagram: @carocode_
# Following a tutorial to get a better understanding of thought process behind
# building a project to later rebuild something myself

import turtle

# Screen Info
screen = turtle.Screen()
screen.title("Tetris by @CaroCode_")
screen.bgcolor("black")
screen.setup(width=600, height=800)
screen.tracer(0)

# Shapes


class shapes():
    def __init__(self):
        self.x = 5
        self.y = 0
        self.color = 2

    def left_move(self, grid):
        grid[self.y][self.x] = 0
        self.x -= 1

    def right_move(self, grid):
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


# creates shapes
shape = shapes()

# puts shapes in grid
grid[shape.y][shape.x] = shape.color

# Draw grid
create_grid(pen, grid)

# Move left and right
screen.listen()
screen.onkeypress(lambda: shape.left_move(grid), "a")
screen.onkeypress(lambda: shape.right_move(grid), "d")


# Main game
while True:
    screen.update()
    # Move the shape
    # Open row
    if shape.y == 23:  # if at bottom row
        shape = shapes()  # make a new shape
    elif grid[shape.y + 1][shape.x] == 0:  # if space below, move
        grid[shape.y][shape.x] = 0  # sets the previous index back to zero
        shape.y += 1  # goes to the next index
        grid[shape.y][shape.x] = shape.color  # gives the color
    else:
        shape = shapes()  # else, make a new shape

    create_grid(pen, grid)

# Keep window open
screen.mainloop()
