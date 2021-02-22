def rotatedDigits(N):
	#change every number to list
	#judge wether or not it is a rotated digits
	#if it is add one
	#return count
	res = []
	arr1 = [2,5,6,9]
	arr2 = [0,1,8]
	#arr3 = [3,4,7]
	for i in range(N+1):
		arr_i = [int(x) for x in str(i)]
		flag = False
		count = 0
		for j in arr_i:
			if j in arr1:
				flag = True
				count += 1
			elif j in arr2:
				count += 1
		if flag == True and count == len(arr_i):
			res.append(i)
	return res
print(rotatedDigits(20))
'''
[1,2,3]
1 0 0 True
[1,8]
'''