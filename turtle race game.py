from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

colours = ["red", "orange", "yellow", "green", "blue", "purple", ]
y_position = [-90, -50, -10, 30, 70, 110]
all_turtle = []

for num in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[num])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[num])
    new_turtle.speed(2)
    all_turtle.append(new_turtle)

rase_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle would win the race?: ").lower()

if user_bet:
    rase_on = True
while rase_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            rase_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won!😃 The {winning_color} turtle is the winner")
            else:
                print(f"You lose!😤 The {winning_color} turtle is the winner")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
