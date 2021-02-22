def nextGreatestLetter(letters, target):
	res = 0
	stack = []
	index = 0
	for i in range(len(letters)):
		if i == len(letters)-1 and letters[i] == target:
			return letters[0]
		elif letters[i] <= target:
			stack.append(letters[i])
			index = i

	 
	print(stack)
	if len(stack) == 0:
		return letters[0]
	elif len(stack) == len(letters):
		return letters[0]

	return letters[index+1]
letters = ["e","e","e","e","e","e","n","n","n","n"]
target = "e"
print(nextGreatestLetter(letters,target))