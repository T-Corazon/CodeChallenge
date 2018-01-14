class Drunk(object):
	def __init__(self,name):
		self.name = name
	def move(self,field,time = 1):
		if field.getDrunk() != self:
			raise ValueError("Drunk.move called with drunk not in the field")
		for i in range(time):
			pt = CompassPt(random.choice(CopassPt.possibles))
			field.move(pt,i)
