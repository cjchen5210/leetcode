nums = [1,2,3,4]

def dominantIndex(nums):
	max_num = 0
	sec_num = 0
	for i in nums:
		if max_num < i:
			sec_num = max_num
			max_num = i
		if i > sec_num and i < max_num:
			sec_num = i
	if max_num >= sec_num * 2 or sec_num == 0:
		return nums.index(max_num)
	else:
		return -1
#print(dominantIndex(nums))


max_num = 0
sec_num = 0
for i in nums:
	if max_num < i:
		sec_num = max_num
		max_num = i
	if i > sec_num and i < max_num:
			sec_num = i
print(max_num,sec_num)