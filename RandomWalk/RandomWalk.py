import math
import matplotlib as plt 
import random
from Location import Location
from CompassPt import CompassPt
from Field import Field
from Drunk import Drunk

def performTrial(time,f):
	start = f.getloc()
	distances = [0,0]
	for t in range(1,time + 1):
		f.getDrunk().move(f)
		newLoc = f.getLoc()
		distance = newLoc.getDist(start)
		distances.append(distance)
	return distances
	
drunk = Drunk(name:'Hipson')
for i in range(J):
	f = Field(drunk,Location(0,0))
	distances = performTrial(500,f)
	plt.plot(distances)
plt.title("Random Walk")
plt.xlabel("Time")
plt.ylabel("Distance from Origin")

plt.show()
