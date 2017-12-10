#~ You're working in a big bank with a lot of money transactions everyday. 
#~ Your boss gave you a task to increase the stability of your system. 
#~ After some thinking you came up with the following way for determining 
#~ the stability of the set of transactions: if you have n transactions, 
#~ ith of which was made for transactionsi dollars, 
#~ the stability coefficient is equal to the minimum to maximum 
#~ transaction amount ratio - the higher it is, 
#~ more stable all transactions are. For example, if transaction amounts 
#~ are transactions = [3, 6, 3, 4, 2], the stability coefficient is 
#~ equal 2 / 6 = 1 / 3, because the minimal transaction has amount 
#~ 2 dollars and maximal - 6 dollars.

#~ To optimize the stability coefficient you decided to split up some 
#~ transactions into two parts. You can take any transaction for x dollars 
#~ and split it up into two parts y and z so that y + z = x
#~ (note that y and z don't have to be integers - for example, 
#~ you can split x = 100 into y = 24.66 and z = 75.34). 
#~ But you can't split up one transaction more than once - otherwise it 
#~ will be quite suspicious. Given the array transactions representing 
#~ the amount of all transactions made in your bank yesterday, return 
#~ the maximal possible stability coefficient that can be obtained using 
#~ your optimizations.

#~ Example

#~ For transactions = [2, 2, 2], the output should be
#~ transactionsStability(transactions) = 1.0.

#~ The initial stability coefficient is equal 1.0 and can't be made bigger.

#~ For transactions = [1, 2, 3], the output should be
#~ transactionsStability(transactions) = 0.66667.

#~ 3 can be splitted into 1.5 and 1.5 and 2 can be splitted into 1 and 1,
 #~ after that stability coefficient will be equal 1 / 1.5 = 0.(6).

#~ Input/Output

#~ [time limit] 4000ms (py3)

#~ [input] array.integer transactions

#~ Array, containing amounts of transactions made in your bank yesterday.

#~ Guaranteed constraints:
#~ 1 <= transactions.length <= 5.105,
#~ 1 <= transactions[i] <= 104.

#~ [output] float

#~ The maximum value of stability coefficient. Your answer will be 
#~ considered correct if its absolute error doesn't exceed 10-5.

def transactionsStability(transactions):
	t = list(set(transactions))
	a = max(t)/2
	t += [a]
	t.sort(reverse=True)
	t = t[1:]
	if a >min(t):
		return min(t)/a
	elif a==min(t):
		return 1
	else:
		return a/min(t)
transactions = [12, 9, 7, 6, 5] 
a = transactionsStability(transactions)
print(a)

import numpy as np
def transactionsStability(transactions):
    t = np.array(transactions)
    half = t/2
    if max(half)>=min(t):
        return min(t)/max(half)
    else:
        return min(t)/max(t)
