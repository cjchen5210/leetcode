def getMaximumGenerated(n):
	vec = [0] * (n+1)
	vec[1] = 1
	for i in range(2,n+1):
		if i % 2 == 0:
			vec[i] = vec[i//2]
		else:
			vec[i] = vec[i//2] + vec[i//2+1]
	return vec
print(getMaximumGenerated(4))