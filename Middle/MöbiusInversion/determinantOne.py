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
	s = 0
	phi=[0 for i in range(n+1)]
	phi[1] = 1
	i = 2
	while i <= n:
		if phi[i] == 0:
			phi[i] = i - 1
			j = 2
			while j * i <=n:
				if phi[j] != 0:
					q = j
					f = i - 1
					while q % i == 0:
						f *= i
						q //= i
					phi[i * j] = f * phi[q]
					#print(i*j,f,phi[q],f * phi[q])
				j += 1
		s += phi[i]
		i += 1
	return ((s*32)%(10**9+7)+20)

## Bassically what we need to know are three things
## 1. when n*b = c*d + 1 has to hold when these number > 1, n must co-prime c,d
## 2. There will be phi(n) terms of co-primes of n where phi is Euler's totient function
## 3. If there is a number c co-prime n, there will be one and only one modular multiplicative inverse
##   number b wher a*b = 1(mod n )
##   https://en.wikipedia.org/wiki/Modular_multiplicative_inverse
## So the problem now becames to sum over the Euler's totient function for n>1 and times 32 + 20 
## the 32 comes from the +- and swap locations of the number. and the resons for the first 20 is that 
## there are 0,0 in the case when n==1 where those are the same for -0,0 and -0,-0 
##
## The way I solved this is using a modified Sieve of Eratosthenes to calcuate the phi fucntion 
## for all the terms from 2 to n 
def wo():
	s = [*range(eval(dir()[0])[0]+1)]
	t = 0 
	for i in s:
		if i==t>1:
			s[::t]=[j*~-t/t for j in s[::t]]
		t += 1
	return sum(s)*32%(10**9+7)-12

#  By now, you may have all figire out the formular, right?
#  It is:
#  A(1) = 20
#  A(N) = A(N-1) + 32 * phi(N),
#      in which phi(N) is the Euler's totient Function, which counts number 
#      of integer in the range [1..N] that is coprime to N
#          Example: phi(1) = 1: only 1 is coprime to 1
#                   phi(2) = 1: only 1 is coprime to 2
#                   phi(6) = 2: 1, 5 coprime to 6
 
#  ===
#  So, it's not so hard to see the first part, A(N) = A(N-1) + something,
#~ right? All soluton that satisfy with (N-1) will also satisfy with (N).
 #~ So, the thing must be proven is that:
#~ #  For given N, number of solutions in which one entry has absolute 
#~ value is N is  '32 * phi(N)'
 
#  Back to the problem, here is the mathematic prove for the formular:
 
 
#  Let the matrix be:
#      [A, B]
#      [C, D]
#  it's determinant will be:
#      det = AD - BC
#  det = 1 will imply the following statements:
#      i)  GCD(A, B) = 1
#          and same with (A, C), (D,B), (D,C)
#          +) because otherwise, we can write A = KX, B = KY with K>0
#             so AD - BC will divisible by K and so K will be an divisor of 1 (which is impossible)
         
#      ii) If there is one entry with absolute value equals N, it will be the ONLY entry with absolute value N
#          +) let take (A = N) for example, 
#              ++) if B or C is N, it will violate i) as GCD(A,B) = N
#              ++) if |D| = N, and |B|, |C| <= N - 1, so 
#                  |BC| <= (N-1)^2 
#                  => |AD - BC| >= |AD| - |BC| >= N*N - (N-1)^2 = 2N - 1 > 1 
#                  so it has no solution if more than 1 entry has absolute value (N)
                 
#  =====
#  So from two statements above, we can easily consider the case |A| = N,
 #~ the other case for B, C, D will stay the same
#~ #  .
#~ #  So let A = N
#~ #  from i) we know that B must be coprime to A and so there is phi(N) 
#~ way to choose the value of B. But we're talking about the range(-N...N)
 #~ so there's must be 2 * phi(N) way to choose B
 
#  AD - BC = 1
#  => D = (BC + 1) / N (as A = N)
#  D is integer => BC + 1 is divisible by N
#  => BC = N - 1 (mod N)
#  => C = (N-1) * B^-1 (mod N)
 
#  Note that, if GCD(B,N) = 1, there is always one and ONLY one value 
#~ of X that BX = 1 or X = B^-1 (mod N). This can be easily proven 
#~ (if there're 2 values => they must be equal modulo N)
 
#~ #  So for a given value of B, there's only one coresspond value of C 
#~ that can make det = 1. But again, we're talking about the range(-N, N) 
#~ so there's 2 way to choose C for each value B.
 
#  So this imply: 
#    2 phi(N) * 2 = 4 phi(N) solutions for A = N.
 
#  Same way of proff for the case A = -N, B = N, C = -N, etc
#  As ii) show, these case are completely disjoint, so there're total 
#~ 32 phi(N) solutions!
 
#~ #  there're many other interesting formulars from this site.
 #~ I would prove them all if I have time. Enjoy!
 
#  https://oeis.org/A002088
 
#  Have good understanding and ask me anything if you like!
 

# n, = eval(dir()[0])
# s = -12
# while n:
#     c = k = n
#     j = 2
#     while c>1:
#         if c%j<1:
#             k -= k/j
#             while c%j<1:
#                 c /= j
#         j = j*j>c and c or j+1
#     s += 32 * k
#     s %= 1e9+7
#     n -= 1
# return s
            
#this solution is implement from another fomular from OEIS, much quicker than the above
#~ n, = eval(dir()[0])
#~ M = {}

#~ def f(m):
    #~ if m not in M:
        #~ s = m*(m+3)/2
        #~ i = 1
        #~ while i < m:
            #~ i += 1
            #~ s -= f(m//i)
        #~ M[m] = s
    #~ return M[m]

#~ return f(n) * 32  % (1e9+7) - 44
