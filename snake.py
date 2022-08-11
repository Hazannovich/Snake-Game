from turtle import Turtle
import time
STARTING_POSITIONS = [0, -20, -40]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_block = Turtle(shape="square")
            new_block.color("white")
            new_block.pu()
            new_block.setx(position)
            self.snake.append(new_block)

    def move(self):
        for block_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[block_num - 1].xcor()
            new_y = self.snake[block_num - 1].ycor()
            self.snake[block_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def add_block(self):
        new_block = Turtle(shape="square")
        new_block.color("white")
        new_block.pu()
        new_block.goto(self.snake[len(self.snake) - 1].position())
        self.snake.append(new_block)

    def reset(self):
        time.sleep(2)
        for block in self.snake:
            block.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
