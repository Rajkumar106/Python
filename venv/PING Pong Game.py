import turtle
import pygame

#Initializations
score_1=0
score_2=0
game_over=False  #variable to track the Game State

# Ball Hitting Sound
pygame.mixer.init()
ball_hit_sound = pygame.mixer.Sound(r"C:\Users\Dell\Downloads\mixkit-basketball-ball-hit-2091.wav")
def ball_hitting_sound():
    ball_hit_sound.play()

# Game Over Sound
game_over_audio = pygame.mixer.Sound(r"C:\Users\Dell\Downloads\mixkit-funny-fail-low-tone-2876.wav")
def game_over_sound():
    game_over_audio.play()

#Setting Display Screen
window=turtle.Screen()
window.setup(800,600)
window.bgcolor("violet")
window.title("Welcome to PONG GAME")
window.tracer(0)   #Dont trace the initial positions

#LEFT Paddle
left_paddle=turtle.Turtle()   #creating a turtle and storing it in a object(left_paddle)
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("purple")
left_paddle.shapesize(stretch_wid=5,stretch_len=1) #Changing the Square shape into Rectangle
left_paddle.penup()  #Penup - dont draw the path line
left_paddle.goto(-380,0)  #setting position

#Right Paddle
right_paddle=turtle.Turtle()   #creating a turtle and storing it in a object(right_paddle)
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("purple")
right_paddle.shapesize(stretch_wid=5,stretch_len=1)
right_paddle.penup()
right_paddle.goto(375,0)

#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(1.3)
ball.color("gray")
ball.penup()
ball.dx=0.45  #Pixels the ball has to move is 0.25 pixels per move
ball.dy=0.45

# Ball Hitting Audio
#ball_hit_audio=r"C:\Users\Dell\Downloads\mixkit-small-hit-in-a-game-2072.wav"
#Score card
pen=turtle.Turtle()
pen.speed(0)
pen.color("purple")
pen.penup()
pen.hideturtle()
pen.goto(0,235)
pen.write("PLAYER-1 : 0 \nPLAYER-2 : 0",align="center",font=("Courier",20,"bold"))

#Moving Paddles
def left_paddle_up():
    y = left_paddle.ycor()
    if y < 240:  # Adjust the upper limit
        left_paddle.sety(left_paddle.ycor()+20) #Modifying paddle using "sety" key word by incrementing the "y coordinate"
def left_paddle_down():
    y=left_paddle.ycor()
    if y>-235:  # Adjust the lower Limit
        left_paddle.sety(left_paddle.ycor()-20) #decrementing the "y coordinate"

def right_paddle_up():
    y = right_paddle.ycor()
    if y<240:
        right_paddle.sety(right_paddle.ycor()+20)
def right_paddle_down():
    y = right_paddle.ycor()
    if y>-235:
        right_paddle.sety(right_paddle.ycor()-20)

#Setting Keys(BUTTON) to move Paddles
window.listen() #using those functions by "Keys"
window.onkeypress(left_paddle_up,"w")
window.onkeypress(left_paddle_down,"s")
window.onkeypress(right_paddle_up,"Up")
window.onkeypress(right_paddle_down,"Down")

while not game_over:
    window.update()
    #Ball Movement
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    #Ball collision in up wall(y coordinate)
    #Up Wall
    if ball.ycor()>285:
        ball.dy*=-1
    #Right Wall
    if ball.xcor()>380:
        ball.dx*=-1
        score_1+=1
        #ball.goto(0,0)
        pen.clear()
        pen.write("PLAYER-1 : {} \nPLAYER-2 : {}".format(score_1,score_2), align="center", font=("Courier", 20, "bold"))
        if score_1 >= 5:
            game_over = True
    #Bottom Wall
    if ball.ycor()<-280:
        ball.dy*=-1
    #Left Wall
    if ball.xcor()<-385:
        ball.dx*=-1
        score_2+=1
        #ball.goto(0,0)
        pen.clear()
        pen.write("PLAYER-1 : {} \nPLAYER-2 : {}".format(score_1,score_2), align="center", font=("Courier", 20, "bold"))
        if score_2 >= 5:
            game_over = True

    #collision on paddles
    if ball.xcor()>360 and right_paddle.ycor()-50 < ball.ycor() < right_paddle.ycor()+50:
        ball.setx(343.5)
        ball.dx *= -1
        ball_hitting_sound()  # This function play the Audio
    if ball.xcor()<-365 and left_paddle.ycor()-50 < ball.ycor() < left_paddle.ycor()+50:
        ball.setx(-343.5)
        ball.dx *= -1
        ball_hitting_sound()
#Game Over message
pen.goto(0,0)
pen.write("GAME OVER!", align="center", font=("Courier", 40, "bold"))
game_over_sound()  # It plays the game over audio
turtle.done()