import turtle

ScreenX = int(input("Resolution of the screen on X: ")) #1270
ScreenY = int(input("Resolution of the screen on Y: ")) #820
List_Of_Triangles = []
List_Of_Dots = []

class POT:
	def __init__(self):
		self.main()

	def main(self):
		self.CreateScreen(ScreenX, ScreenY, "black")
		self.CreateTriangle()
		self.UpdateScreen()

	def CreateDots(self, ID):
		Triangle = List_Of_Triangles[ID]

		Triangle_Left = (Triangle.xcor()-6, Triangle.ycor())
		Triangle_Right = (Triangle.xcor()+6, Triangle.ycor())

		ID = 0
		Do_Not_Spawn = 0
		for Dot in List_Of_Dots:
			if(Dot.distance(Triangle_Left) < 1):
				List_Of_Dots.pop(ID)
				Do_Not_Spawn = 1
			if(Dot.distance(Triangle_Right) < 1):
				List_Of_Dots.pop(ID)
				Do_Not_Spawn = 1
			ID += 1

		Times = 0
		T = 2
		if(Do_Not_Spawn == 1):
			Times = 1
			T = 1
		for i in range(T):
			Dot = turtle.Turtle()
			Dot.hideturtle()
			Dot.penup()
			Dot.shape("circle")
			Dot.shapesize(0.1, 0.1)
			if Times == 0:
				Dot.goto(Triangle_Left)
			else:
				Dot.goto(Triangle_Right)
			List_Of_Dots.append(Dot)
			Times += 1

	def CreateSingleTriangle(self, PosX, PosY):
		T = turtle.Turtle()
		T.hideturtle()
		T.shape("arrow")
		T.shapesize(0.6, 1.4)
		T.color("white")
		T.penup()
		T.goto(PosX, PosY)
		T.left(90)
		T.showturtle()
		List_Of_Triangles.append(T)

	def CreateTriangle(self):
		ID = 0
		self.CreateSingleTriangle(0, ScreenY/2 - 7)
		self.CreateDots(ID)
		ID += 1
		while True:
			for Dot in List_Of_Dots:
				self.CreateSingleTriangle(Dot.xcor(), Dot.ycor()-15)
				self.CreateDots(ID)
				ID += 1

	def CreateScreen(self, SizeX, SizeY, Color):
		Screen = turtle.Screen()
		Screen.setup(SizeX, SizeY)
		Screen.bgcolor(Color)
		print("Ctrl + C to exit program!")

	def UpdateScreen(self):
		while True:
			turtle.Screen().update()

if __name__ == "__main__":
	POT()