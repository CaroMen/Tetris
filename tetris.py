# Instagram: @carocode_
# Following a tutorial to get a better understanding of thought process behind
# building a project to later rebuild something myself

import turtle
import time
import random

# Screen Info
screen = turtle.Screen()
screen.title("Tetris by @CaroCode_")
screen.bgcolor("white")
screen.setup(width=600, height=800)
screen.tracer(0)

delay = 0.10

# Shapes


class shapes():
    def __init__(self):
        self.x = 5
        self.y = 0
        self.color = random.randint(1, 7)

        # Block shape
        square = [[1, 1],
                  [1, 1]]

        horiz_line = [[1, 1, 1, 1]]

        vert_line = [[1],
                     [1],
                     [1],
                     [1]]

        left_l = [[1, 0, 0, 0],
                  [1, 1, 1, 1]]

        right_l = [[0, 0, 0, 1],
                   [1, 1, 1, 1]]

        right_s = [[0, 1, 1],
                   [1, 1, 0]]

        left_s = [[1, 1, 0],
                  [0, 1, 1]]

        t = [[0, 1, 0],
             [1, 1, 1]]

        obj_shapes = [square, horiz_line, vert_line,
                      left_l, right_l, right_s, left_s, t]

        # Choose a random shape each time
        self.shape = random.choice(obj_shapes)

        self.height = len(self.shape)
        self.width = len(self.shape[0])

    def left_move(self, grid):
        if self.x > 0:
            if grid[self.y][self.x - 1] == 0:
                self.erase_shape(grid)
                self.x -= 1

    def right_move(self, grid):
        if self.x < 12 - self.width:  # keeps it from going off grid
            # checks to see if there's something in the way
            if grid[self.y][self.x + self.width] == 0:
                self.erase_shape(grid)
                self.x += 1

    def draw_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if (self.shape[y][x] == 1):
                    grid[self.y + y][self.x + x] = self.color

    def erase_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if (self.shape[y][x] == 1):
                    grid[self.y + y][self.x + x] = 0

    def collision(self, grid):
        for x in range(self.width):
            # check if bottom is 1
            if (self.shape[self.height - 1][x] == 1):
                if (grid[self.y + self.height][self.x + x] != 0):
                    return False
        return True

    def rotate(self, grad):
        # First erase_shape
        self.erase_shape(grid)
        rotated_shape = []
        for x in range(len(self.shape[0])):
            new_row = []
            for y in range(len(self.shape) - 1, -1, -1):
                new_row.append(self.shape[y][x])
            rotated_shape.append(new_row)

        right_side = self.x + len(rotated_shape[0])
        if right_side < len(grid[0]):
            self.shape = rotated_shape
            # Update the height and width
            self.height = len(self.shape)
            self.width = len(self.shape[0])


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
    pen.color("black")
    pen.hideturtle()
    pen.goto(-75, 350)
    pen.write("Score: {}".format(score), move=False,
              align="left", font=("Arial", 24, "normal"))


# creates shapes
shape = shapes()

# puts shapes in grid
grid[shape.y][shape.x] = shape.color

# Draw grid
#create_grid(pen, grid)

# Move left and right
screen.listen()
screen.onkey(lambda: shape.left_move(grid), "a")
screen.onkey(lambda: shape.right_move(grid), "d")
screen.onkey(lambda: shape.rotate(grid), "space")

# Set score to zero
score = 0
draw_score(pen, score)

# Main game
while True:
    screen.update()
    # Move the shape
    # Open row
    # Check for bottom
    if shape.y == 23 - shape.height + 1:  # if at bottom row
        shape = shapes()  # make a new shape
        check_grid(grid)
    # Check for collision with next row
    elif shape.collision(grid):  # if space below, move
        # Erase current shape
        shape.erase_shape(grid)
        # Move shape by 1
        shape.y += 1  # goes to the next index
        # Draw shape again
        shape.draw_shape(grid)
    else:
        shape = shapes()  # else, make a new shape
        check_grid(grid)

    # draw screen and score
    create_grid(pen, grid)
    draw_score(pen, score)

    time.sleep(delay)

# Keep window open
screen.mainloop()
