from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.pu()
        self.goto(0, 270)
        self.color("white")
        with open("score.txt") as file:
            self.high_score = int(file.read())
        self.write(f"Score: {self.score}   High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("score.txt", 'w') as file:
                file.write(str(self.score))
        self.score = -1
        self.update_score()

