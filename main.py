from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

# creating a screen object
screen = Screen()
# setting up the screen size
screen.setup(800, 600)
# setting the screen background
screen.bgcolor("black")
# giving it a name
screen.title("Pong")

# using tracer method to hide the animation
# And it is called before your animation(movement)
screen.tracer(0)

# creating paddle object
right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
right_paddle.move("Up", "Down")
left_paddle.move("w", "s")

# creating a ball object
ball = Ball()

# score object
score = Score()

# using this to update the turtle, so you can see what you created
game_is_on = True
while game_is_on:
	time.sleep(0.1)  # makes things slow a bit
	screen.update()
	ball.move()

	# detecting collision with wall
	if ball.ycor() > 280 or ball.ycor() < -280:
		ball.bounce_y()

	# Detect collision with right_paddle
	if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
		ball.nitro += 1
		ball.bounce_x()

	# detect if right paddle misses
	if ball.xcor() > 380:
		ball.reset_position()
		score.l_point()

	# detect if the left paddle misses
	if ball.xcor() < -380:
		ball.reset_position()
		score.r_point()

screen.exitonclick()
