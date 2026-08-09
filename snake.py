from turtle import Turtle
STARTING_POS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for pos in STARTING_POS:
            seg=Turtle(shape="square")
            seg.color("white")
            seg.penup()
            seg.setposition(pos)
            self.segments.append(seg)

    def move(self):
        for s_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[s_num-1].xcor()
            new_y = self.segments[s_num - 1].ycor()
            self.segments[s_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

