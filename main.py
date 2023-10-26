import turtle
import random
import time

background = turtle.Screen()
background.screensize(250, 200, bg="light blue")

score = 0
score_board = turtle.Turtle()
myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
myTurtle.penup()
myTurtle.shapesize(2, 2)
myTurtle.color("green")
countdownTurtle = turtle.Turtle()
countdownTurtle.hideturtle()
gameOver = False

def setupScoreTurtle():
    topHeight = background.window_height() / 2

    y = topHeight * 0.9

    score_board.hideturtle()
    score_board.color("black")
    score_board.penup()
    score_board.goto(0, y)
    score_board.write(arg="Skor:0", align="center", font=("Courier", 24, "normal"))

setupScoreTurtle()

def countdown(t):
    global gameOver
    topHeight = background.window_height() / 2

    y = topHeight * 0.9

    countdownTurtle.hideturtle()
    countdownTurtle.color("Blue")
    countdownTurtle.penup()
    countdownTurtle.goto(0, y - 30)
    countdownTurtle.clear()
    if t > 0:
        countdownTurtle.clear()
        countdownTurtle.write(arg="Countdown:{}".format(t), align="center", font=("Courier", 24, "normal"))
        background.ontimer(lambda: countdown(t - 1), 1000)
    else:
        gameOver = True
        myTurtle.hideturtle()
        countdownTurtle.clear()
        countdownTurtle.write(arg="Game Over!", align="center", font=("Courier", 24, "normal"))

def action():
    def handleClick(x, y):

        global score
        score += + 1
        score_board.clear()
        score_board.write("Score: {}".format(score), move=False, align="center", font=("Courier", 24, "normal"))
        print(x, y)

    if not gameOver:
        for i in range(21):
            myTurtle.onclick(handleClick)
            x = random.randint(-370, 370)
            y = random.randint(-370, 370)
            myTurtle.hideturtle()
            myTurtle.goto(x, y)
            myTurtle.showturtle()
            time.sleep(0.5)

countdown(20)
action()
background.mainloop()
