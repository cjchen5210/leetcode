def minimumAbsDifference(arr):
	sorted_arr = sorted(arr)
	distinct = 10000
	res = []
	for i in range(len(sorted_arr)-1):
		if sorted_arr[i+1] - sorted_arr[i] < distinct:
			distinct = sorted_arr[i+1] - sorted_arr[i]
	print(sorted_arr)
	print(distinct)
	for i in range(len(sorted_arr)-1):
		if sorted_arr[i+1] - sorted_arr[i] == distinct:
			temp = []
			temp.append(sorted_arr[i])
			temp.append(sorted_arr[i+1])
			res.append(temp)
	return res

arr = [3,8,-10,23,19,-4,-14,27]
print(minimumAbsDifference(arr))




