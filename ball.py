from turtle import Turtle


class Ball(Turtle):
	def __init__(self):
		super().__init__()
		self.pu()
		self.shape("circle")
		self.color("pink")
		self.x_move = 10
		self.y_move = 10
		self.nitro = 0.1

	def move(self):
		new_x = self.xcor() + self.x_move
		new_y = self.ycor() + self.y_move
		self.goto(new_x, new_y)

	def bounce_y(self):  # reverses the y_cor to change direction
		self.y_move *= -1

	def bounce_x(self):
		self.x_move *= -1
		self.nitro *= 0

	def reset_position(self):
		self.goto(0, 0)
		# self.nitro = 0.1  # when we are resetting, we want to go back to the normal speed to avoid over speeding
		self.bounce_x()
