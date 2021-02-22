
#1
values = [2, 4, 1, 5, 9, 2, 0, 6]
temp = values[0]
print('-' * values[0])#output the first element
for k in range(1,len(values)):
    if values[k] <= temp:
    	pass     
    elif temp < values[k]:
        print('-' * values[k])
        temp = values[k]
print(values)

#2
values = [2, 4, 1, 5, 9, 2, 0, 6]
def greedy(values):
	head = values[0]
	res = []
	#temp = []
	sign = '-'
	#temp.append(sign * values[0])
	res.append(sign * values[0])
	for i in range(1,len(values)):
		if head < values[i]:
			#temp = []
			#temp.append(sign * values[i])
			res.append(sign * values[i])
			head = values[i]
	return res
for s in greedy(values):
	print(s)
