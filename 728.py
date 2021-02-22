def selfDividingNumbers(left, right):
	res = []
	for i in range(left, right+1):
		if dividing(i) != None:
			res.append(dividing(i))
	return res

def dividing(nums):
	str_nums = str(nums)
	if '0' in str_nums:
		return None
	if nums <= 9 and nums >0:
		return nums
	count = 0
	for ele in str_nums:
		if nums % int(ele) == 0:
			count += 1
	if count == len(str_nums):
		return nums
	else:
		return None

print(selfDividingNumbers(1,22))