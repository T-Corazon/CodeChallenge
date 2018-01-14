class Location(object):
	def __init__(self,x,y):
		self.x = float(x)
		self.y = float(y)
	def move(self,x,y):
		return Location(self.x + float(xc),self.y + float(yc))
	def getCoords(self):
		return self.x, self.y
	def getDist(self,other)
		xDist = self.x - other.x
		yDist = self.y - other.y
		return math.sqrt(xDist ** 2 + yDist ** 2)

