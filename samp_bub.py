op = [5, 4, 6, 1, 9, 15, 12, 11, 2]

print(op)
for i in range(len(op)):
	for j in range(i):
		if(op[i] < op[j]):
			temp = op[i]
			op[i] = op[j]
			op[j] = temp


print("Last result : ", op)
