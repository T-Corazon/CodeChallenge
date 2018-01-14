#~ import math
from matplotlib import pyplot as plt
#~ import random
from Location import Location
#~ from CompassPt import CompassPt
from Field import Field
from Drunk import Drunk

def performTrial(time,f):
	start = f.getLoc()
	distances = [0.0]
	for t in range(1,time + 1):
		f.getDrunk().move(f)
		newLoc = f.getLoc()
		distance = newLoc.getDist(start)
		distances.append(distance)
	return distances
	
drunk = Drunk('Hipson')
for i in range(1):
	f = Field(drunk,Location(0,0))
	distances = performTrial(500,f)
	plt.plot(distances)
plt.title("Random Walk")
plt.xlabel("Time")
plt.ylabel("Distance from Origin")

plt.show()
