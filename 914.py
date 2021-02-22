
def hasGroupsSizeX(deck) -> bool:
	stack = []
	count = 0
	for num in deck:
		if num == deck[0]:
			count += 1
	for num in deck:
		if len(stack) == 0 or stack[len(stack)-1] == num:
			

inputl = [0,0,0,1,1,1,2,2,2]    
print(hasGroupsSizeX(inputl))
                