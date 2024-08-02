from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as r_data:  # Getting the score from the data.txt file in the project folder
            self.highest_score = int(r_data.read())  # as an integer
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highest Score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def resect_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            # Writing the highest score to the data.txt file in the project folder
            with open("data.txt", mode="w") as w_data:
                w_data.write(f'{self.highest_score}')
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
