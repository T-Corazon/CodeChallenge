callnumber = 0
def maxval(v,m,i,am):
	global callnumber
	callnumber += 1
	if i == 0:
		if m[i] <= am:
			return v[i]
		return 0
	without_i = maxval(v,m,i-1,am)
	if m[i] > am:
		return without_i
	else:
		with_i = v[i] + maxval(v,m,i-1,am-m[i])
	return max(without_i,with_i)
	
def fastmaxval(v,m,i,am,l):
	global callnumber
	callnumber += 1
	try:
		return(l[(i,am)])
	except KeyError:
		if i == 0:
			if m[i] <= am:
				l[(i,am)] = v[i]
				return v[i]
			else:
				l[(i,am)] = 0
				return 0
		without_i = fastmaxval(v,m,i-1,am,l)
		if m[i] > am:
			l[(i,am)] = without_i
			return without_i
		else:
			with_i = v[i] + fastmaxval(v,m,i-1,am-m[i],l)
			res = max(without_i,with_i)
			l[(i,am)] = res
		return res

def data(v,m,i,am):
	l = {}
	return fastmaxval(v,m,i,am,l)
m = [5,3,2,2,9,8,6,3,4,2,7,5,6,9,5]
v = [9,7,8,8,7,8,7,8,20,1,2,5,6,3,1]
i = len(m) - 1
am = 5
print("value: " + str(maxval(v,m,i,am)) + "\nfunction call: " + str(callnumber))
callnumber = 0
print("value: " + str(data(v,m,i,am)) + "\nfunction call: " + str(callnumber))

