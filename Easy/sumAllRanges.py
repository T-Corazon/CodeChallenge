#~ Given an array array of positive integers, calculate the sum over 
#~ the closed ranges defined by all the possible pairs in array. 
#~ Since this sum can be very large, return it modulo 109 + 7.

#~ Example

#~ For array = [1, 5, 2], the output should be
#~ sumAllRanges(array) = 32.
#~ We can define the following valid ranges: [1, 5], [1, 2], [2, 5]. 
#~ The sum over all those ranges is sum([1..5]) + sum([1..2]) + sum([2..5])
 #~ = (1 + 2 + 3 + 4 + 5) + (1 + 2) + (2 + 3 + 4 + 5) = 32.

#~ For array = [4, 2, 4, 3], the output should be
#~ sumAllRanges(array) = 41.
#~ The solution is sum([2..3]) + sum([2..4]) + sum([2..4]) + 
#~ sum([3..4]) + sum([3..4]) + sum([4..4]) = 41.

#~ Input/Output

#~ [time limit] 4000ms (py3)
#~ [input] array.integer array

#~ Array of positive integers.

#~ Guaranteed constraints:
#~ 0 <= array.length <= 105,
#~ 0 <= array[i] <= 106.
#~ n = s = c = 0
#~ for i in sorted(eval(dir()[0])[0]):
    #~ s -= n*i*~i+c
    #~ c += i*i-i
    #~ n += 1
#~ return s//2%(10**9+7)

def sumAllRanges(array):
	s = 0
	array.sort()
	len_i = len(array)
	len_j = len(array)
	for i in range(len_i):
		t = array[i]
		for j in range(1,len_j):
			m = array[i+j]
			if t == m:
				s += t
			else:
				s += (t+m)*(m-t+1)/2
		len_j -= 1
	return s%(10**9+7)
	
#~ array = input("Enter your array:")
array = [23614,24938,96731,869736]
print(sumAllRanges(array))
