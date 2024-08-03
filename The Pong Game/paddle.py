from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_pos, y_pos)

    # Move paddle up and down
    def r_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def r_down(self):
        self.goto(self.xcor(), self.ycor() - 20)

    def l_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def l_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
