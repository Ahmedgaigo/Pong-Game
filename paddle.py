from turtle import Turtle, Screen


class Paddle(Turtle):  # creating a paddle class which inherits from the turtle class
	def __init__(self, x, y):
		super().__init__()
		self.x = x
		self.y = y
		self.screen = Screen()

		self.pu()
		self.color("white")
		self.shape("square")
		self.left(90)
		self.shapesize(1, 5)
		self.goto(x, y)

	def move(self, a, b):
		"""'a' is the key to move up, and 'b' is the key to move down"""
		self.screen.listen()
		self.screen.onkeypress(self.up, a)
		self.screen.onkeypress(self.down, b)

	def up(self):
		self.fd(20)

	def down(self):
		self.bk(20)
