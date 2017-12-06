#~ You are given five points in the form 
#~ (p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y, p5x, p5y). 
#~ Find the area of the ellipse passing through these points.

#~ It is guaranteed that exactly one non-degenerate ellipse can be formed
 #~ with the five points.

#~ Example
#~ For points = [2, -2, -1, -1, 1, -2, -1, 0, 1, -1], the output should be
#~ ellipticSystem(points) = 3.6275987284684357.
#~ These points define a rotated ellipse centered at (0, -1), 
#~ with major axis length 4.50349531674054 and 
#~ minor axis length 1.025603854043734, for an area of 3.627598728468436.

#~ Input/Output

#~ [time limit] 4000ms (py3)
#~ [input] array.integer points

#~ Array of ten integers defining the five points.

#~ Guaranteed constraints:
#~ points.length = 10,
#~ -100 <= points[i] <= 100.

#~ [output] float
#~ The area of the ellipse formed by these points.

import math
import numpy as np
def ellipticSystem(points):
	array_x = []
	array_y = []
	for i in range(0,10,2):
		array_x.append(points[i])
		array_y.append(points[i+1])
	#~ A * X = b, b=array[-1,-1,-1,-1,-1]
	list_all = []
	for x,y in zip(array_x,array_y):
		j = [x**2,x*y,y**2,x,y]
		list_all.append(j)
	matrix_A = np.mat(list_all)
	det_A = np.linalg.det(matrix_A)
	list_abcde = []
	for i in range(5):
		matrix_C = matrix_A.copy()
		for j in range(5):
			matrix_C[j,i] = -1
		det_C = np.linalg.det(matrix_C)
		list_abcde.append(det_C / det_A)
	[a,b,c,d,e] = list_abcde
	#~ center point(X_c,Y_c)
	t1 = (4 * a * c - b**2)
	X_c = (b * e - 2 * c * d) / t1
	Y_c = (b * d - 2 * a * e) / t1
	t2 = math.sqrt((a - c)**2 + b**2)
	t3 = 2 *(a * X_c**2 + c * Y_c**2 + b * X_c * Y_c - 1)
	return math.pi * abs(t3) / math.sqrt(abs((a + c + t2) * (a + c - t2 )))

points = [2, -2, -1, -1, 1, -2, -1, 0, 1, -1]
a=ellipticSystem(points)
print(a)
