def nextGreaterElement(nums1, nums2):
	stack, hashmap = [], {}
	res = []
	for num in nums2:
		while (len(stack) != 0) and (stack[-1] < num):
			hashmap[stack.pop()] = num
		stack.append(num)
	print(hashmap)
	print(stack)
	for i in range(len(nums1)):
		if nums1[i] in hashmap.keys():
			res.append(hashmap[nums1[i]])
		else:
			res.append(-1)
	return res

nums1 = [2,4]
nums2 = [4,2,1,3]
print(nextGreaterElement(nums1,nums2))