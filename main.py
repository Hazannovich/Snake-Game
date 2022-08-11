from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Classic")
    screen.tracer(0)
    snake = Snake()
    food = Food()
    board = Scoreboard()
    screen.listen()
    screen.onkey(key="Up", fun=snake.move_up)
    screen.onkey(key="Down", fun=snake.move_down)
    screen.onkey(key="Right", fun=snake.move_right)
    screen.onkey(key="Left", fun=snake.move_left)

    game_is_on = True
    score = 0
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        if snake.head.distance(food) < 15:
            board.update_score()
            snake.add_block()
            food.new_location()
        if snake.head.ycor() > 280 or snake.head.ycor() < -280 \
                or snake.head.xcor() > 280 or snake.head.xcor() < -280:
            board.reset()
            snake.reset()
            screen.update()
            time.sleep(2)
        for block in snake.snake[1:]:
            if snake.head.distance(block) < 10:
                board.reset()
                snake.reset()
                screen.update()
                time.sleep(1)

    screen.exitonclick()
