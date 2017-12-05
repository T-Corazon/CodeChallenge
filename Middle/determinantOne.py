#~ Given a positive integer n, calculate the number of 2 x 2 integer 
#~ matrices with determinant 1 and all entries less than or equal to n in 
#~ absolute value. Return the number modulo 109 + 7.

#~ Example

#~ For n = 1, the output should be
#~ determinantOne(n) = 20.
#~ There are 20 2 x 2 matrices with determinant 1 and all entries 
#~ less than or equal to 1 in absolute value:
#~ [[-1, -1], [0, -1]], [[-1, -1], [1, 0]],
#~ [[-1, 0], [-1, -1]], [[-1, 0], [0, -1]],
#~ [[-1, 0], [1, -1]], [[-1, 1], [-1, 0]],
#~ [[-1, 1], [0, -1]], [[0, -1], [1, -1]],
#~ [[0, -1], [1, 0]], [[0, -1], [1, 1]],
#~ [[0, 1], [-1, -1]], [[0, 1], [-1, 0]],
#~ [[0, 1], [-1, 1]], [[1, -1], [0, 1]],
#~ [[1, -1], [1, 0]], [[1, 0], [-1, 1]],
#~ [[1, 0], [0, 1]], [[1, 0], [1, 1]],
#~ [[1, 1], [-1, 0]], [[1, 1], [0, 1]]
#~ For n = 2, the output should be
#~ determinantOne(n) = 52.
#~ There are 52 2 x 2 matrices with determinant 1 and all entries 
#~ less than or equal to 2 in absolute value:
#~ [[-2, -1], [-1, -1]], [[-2, -1], [1, 0]],
#~ [[-2, 1], [-1, 0]], [[-2, 1], [1, -1]],
#~ [[-1, -2], [0, -1]], [[-1, -2], [1, 1]],
#~ [[-1, -1], [-1, -2]], [[-1, -1], [0, -1]],
#~ [[-1, -1], [1, 0]], [[-1, -1], [2, 1]],
#~ [[-1, 0], [-2, -1]], [[-1, 0], [-1, -1]],
#~ [[-1, 0], [0, -1]], [[-1, 0], [1, -1]],
#~ [[-1, 0], [2, -1]], [[-1, 1], [-2, 1]],
#~ [[-1, 1], [-1, 0]], [[-1, 1], [0, -1]],
#~ [[-1, 1], [1, -2]], [[-1, 2], [-1, 1]],
#~ [[-1, 2], [0, -1]], [[0, -1], [1, -2]],
#~ [[0, -1], [1, -1]], [[0, -1], [1, 0]],
#~ [[0, -1], [1, 1]], [[0, -1], [1, 2]],
#~ [[0, 1], [-1, -2]], [[0, 1], [-1, -1]],
#~ [[0, 1], [-1, 0]], [[0, 1], [-1, 1]],
#~ [[0, 1], [-1, 2]], [[1, -2], [0, 1]],
#~ [[1, -2], [1, -1]], [[1, -1], [-1, 2]],
#~ [[1, -1], [0, 1]], [[1, -1], [1, 0]],
#~ [[1, -1], [2, -1]], [[1, 0], [-2, 1]],
#~ [[1, 0], [-1, 1]], [[1, 0], [0, 1]],
#~ [[1, 0], [1, 1]], [[1, 0], [2, 1]],
#~ [[1, 1], [-2, -1]], [[1, 1], [-1, 0]],
#~ [[1, 1], [0, 1]], [[1, 1], [1, 2]],
#~ [[1, 2], [-1, -1]], [[1, 2], [0, 1]],
#~ [[2, -1], [-1, 1]], [[2, -1], [1, 0]],
#~ [[2, 1], [-1, 0]], [[2, 1], [1, 1]]
#~ Input/Output

#~ [time limit] 4000ms (py3)
#~ [input] integer n

#~ A positive integer. The bound for the absolute values of the
 #~ entries of the matrices being counted.

#~ Guaranteed constraints:
#~ 1 <= n <= 105.

#~ [output] integer

#~ The number (modulo 109 + 7) of 2 x 2 integer matrices with determinant
 #~ 1 and all entries less than or equal to n in absolute value.
 
#~ def determinantOne(n):
	#~ l = range(-n,n+1)
	#~ s = 0
	#~ for a in l:
		#~ for b in l:
			#~ for c in l:
				#~ for d in l:
					#~ if a * b - c * d == 1:
						#~ s += 1
	#~ return s
def determinantOne(n):
	mod = (10**9 + 7)
	s = 0
	for a in range(n+1):
		for b in range(1,n+1):
			for c in range(-n,0):
	return (4 * s) % mod
	
print(determinantOne(12))
 
