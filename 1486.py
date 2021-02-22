def xorOperation(n, start):
	if n == 1:
		return start
	nums = [0] * n
	for i in range(n):
		nums[i] = start + 2*i
	bitwise = nums[0] ^ nums[1]

	for i in range(2,n):
		bitwise = nums[i] ^ bitwise

	return bitwise

print(xorOperation(5,0))