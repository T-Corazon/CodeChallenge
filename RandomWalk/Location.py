import math

class Location(object):
	def __init__(self,x,y):
		self.x = float(x)
		self.y = float(y)
	def move(self,xc,yc):
		return Location(self.x + float(xc),self.y + float(yc))
	def getCoords(self):
		return self.x, self.y
	def getDist(self,other):
		ox, oy = other.getCoords()
		xDist = self.x - ox
		yDist = self.y - oy
		return math.sqrt(xDist ** 2 + yDist ** 2)

