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
v = [9,7,8,8,7,8,7,8,2,1,2,5,6,3,1]
i = len(m) - 1
am = 5
print("value: " + str(maxval(v,m,i,am)) + "\nfunction call: " + str(callnumber))
callnumber = 0
print("value: " + str(data(v,m,i,am)) + "\nfunction call: " + str(callnumber))

def fastmaxval2(v,m,size_v,i,am,av,l):
	global callnumber
	callnumber += 1
	try:
		return(l[(i,am,av)])
	except KeyError:
		if i == 0:
			if m[i] <= am:
				l[(i,am,av)] = v[i]
				return v[i]
			else:
				l[(i,am,av)] = 0
				return 0
		without_i = fastmaxval2(v,m,size_v,i-1,am,av,l)
		if m[i] > am or size_v[i] > av:
			l[(i,am,av)] = without_i
			return without_i
		else:
			with_i = v[i] + fastmaxval2(v,m,size_v,i-1,am-m[i],av-size_v[i],l)
			res = max(without_i,with_i)
			l[(i,am,av)] = res
		return res

def data2(v,m,size_v,i,am,av):
	l = {}
	return fastmaxval2(v,m,size_v,i,am,av,l)
m = [5,3,2,2,9,8,6,3,4,2,7,5,6,9,5]
v = [9,7,8,8,7,8,7,8,2,1,2,5,6,3,1]
size_v = [50,8,90,6,30,1,40,70,5,3,90,9,50,6,90]
i = len(m) - 1
am = 5
av = 10
callnumber = 0
print("value: " + str(data2(v,m,size_v,i,am,av)) + "\nfunction call: " + str(callnumber))
