import numpy as np
#accept a list then transfer it to array
# e ==> efficiency p ==> position a ==> assist
def HungarianAlgorithm(e_list):
	# n, m = e_matrix.shape ==> n==m
	n = len(e_list)
	p_mat = np.zeros((n,n),int)
	e_mat = np.mat(e_list)
	e_mat_2 = e_mat[:,:]
	#delete min elem in each raw
	for i in range(n):
		e_mat_2[:,i] -= min(e_mat_2[:,i])
	#delete min elem in each column
	for j in range(n):
		e_mat_2[j,:] -= min(e_mat_2[j,:])
	# do while when the number of mathced worker < jobs
	# use lines as less as possible to cover all '0'
	p_mat[e_mat_2 == 0] = 3
	for k in range(n):
		num_zero = n - np.count_nonzero(e_mat_2[k,:])
		if num_zero == 1:
			p_mat[
	while 1:
		#choose one of '0' in each raw/column and abandon others
		
		#if num_matched < num_rank ==> get the remain of matrix,do the same
		if (...):
		#if num_matched == num_rank ==> return the matched_matrix[:,:]
		elif (...):
