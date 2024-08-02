from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Lonasctech Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

user_choice = screen.textinput(title="The Lonasctech Snake Game",
                               prompt="Do you want to play the snake game? (y/n): ").lower()

if user_choice == "y" or user_choice == "yes":

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food and reposition the food once collided
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend_segment()
            scoreboard.increase_score()

        # Detect collision with the wall and print game over!
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -280:
            scoreboard.resect_score()
            snake.resect_snake()

        # Detect collision with tail and print game over!
        for segment in snake.segments[1:]:  # using python slicing
            if snake.head.distance(segment) < 10:
                scoreboard.resect_score()
                snake.resect_snake()

screen.exitonclick()
