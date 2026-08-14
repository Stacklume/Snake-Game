from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}",move=False,align="center", font=("Times New Roman",25,'normal'))
    def update(self):
        self.write(f"Score: {self.score}", move=False, align="center", font=("Times New Roman", 25, 'normal'))
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="center", font=("Times New Roman", 25, 'normal'))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update()
