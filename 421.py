def findMaximumXOR(nums):
	vec = []
	for i in range(len(nums)):
		for j in range(i+1,len(nums)):
			vec.append(nums[i] ^ nums[j])
	return max(vec)
nums = [3,10,5,25,2,8]
print(findMaximumXOR(nums))