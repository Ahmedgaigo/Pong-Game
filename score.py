from turtle import Turtle


class Score(Turtle):
	def __init__(self):
		super().__init__()
		self.l_score = 0
		self.r_score = 0
		self.color("white")
		self.pu()
		self.hideturtle()
		self.update_score()

	def update_score(self):
		self.clear()  # clears the score to write the new one
		# position for l_score
		self.goto(-100, 200)
		self.write(f"{self.l_score}", False, "center", ("Courier", 80, "normal"))

		# position for r_score
		self.goto(100, 200)
		self.write(f"{self.r_score}", False, "center", ("Courier", 80, "normal"))

	def l_point(self):
		self.l_score += 1
		self.update_score()

	def r_point(self):
		self.r_score += 1
		self.update_score()

