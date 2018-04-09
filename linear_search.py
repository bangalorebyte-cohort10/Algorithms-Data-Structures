def linear(array, item):
	for i in range(len(array)):
		if(item == array[i]):
			return (i+1)
		
	return ("Not Found")

inp = input('Enter the elements of the list:').split()
print(inp)
maps = map(int, inp)
print(maps)
arr = list(maps)
print(arr)
v = int(input("Enter the element to be found"))
print(v, "found at", linear(arr, v))