# import sys
A = [3, 2, 9, 1, 5]
print("Intial: ", A)
for i in range(len(A)):
	m = i
	for j in range(i+1, len(A)):
		if A[m] > A[j]:
			m = j
	A[i], A[m] = A[m], A[i]
	print("iteration",i+1, ":", A)

print ("Sorted array")
print(A)