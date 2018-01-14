class Field(object):
	def __init__(self,drunk,loc):
		self.drunk = drunk
		self.loc = loc
	def move(self,cp,dist):
		oldLoc = self.loc
		xc, yc = cp.move(dist)
		self.loc = oldLoc.move(xc,yc)
	def getLoc(self):
		return self.loc
	def getDrunk(self):
		return self.drunk
