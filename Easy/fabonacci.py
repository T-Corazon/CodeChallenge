#fabonacci 0 1 1 2 3 5 ...
callnumber = 0
def fabonacci(n):
	global callnumber
	#~ try:
		#~ type(n)== type(1)
	#~ except TypeError:
		#~ print("You must enter an integer")
	#~ else:
		#~ callnumber += 1
	callnumber += 1
	if n == 0:
		return 0
	elif n <= 2:
		return 1
	else:
		return fabonacci(n-1)+fabonacci(n-2)

def fastfabonacci(n,memory_data):
	global callnumber
	#~ try:
		#~ type(n)== type(1)
	#~ except TypeError:
		#~ print("You must enter an integer")
	#~ else:
		#~ callnumber += 1
	callnumber += 1
	if n not in memory_data:
		memory_data[n] = fastfabonacci(n-1,memory_data)+fastfabonacci(n-2,memory_data)
	return memory_data[n]
	
def fab_memory(n):
	memory_data = {0:0,1:1,2:1}
	return fastfabonacci(n,memory_data)
n = 20
#~ print("The value: {0} The callnumber: {1}".format(fabonacci(n),callnumber))
#~ callnumber = 0
#~ print("The value: {0} The callnumber: {1}".format(fab_memory(n),callnumber))

def gemPower(n):
	d = {1:3,2:7,3:17,4:41,5:99}
	if n not in d:
		d[n] = (2 * gemPower(n-1) + gemPower(n-2))
	return d[n]
print(gemPower(n))
