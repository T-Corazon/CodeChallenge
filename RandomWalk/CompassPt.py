class CompassPt(object):
	possibles = ('N','S','W','E')
	def __init__(self,pt):
		if pt in self.possibles:
			self.pt = pt
		else:
			raise ValueError("in CompassPt.__init__")
	def move(self,dist):
		if self.pt == 'N':return (0,dist)
		elif self.pt == 'S':return (0,-dist)
		elif self.pt == 'W':return (-dist,0)
		elif self.pt == 'E':return (dist,0)
		else:
			raise ValueError("in CompassPt.move")
