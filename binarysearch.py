#!/usr/bin/env python3
import time
import timeit

mylist = [10, 20, 30, 40, 50, 63, 78, 99, 102, 190,200]

def recursivebinary(key,low,upper):
    
    middle = (low+upper)//2
    if (key == mylist[middle]):
            return middle
    elif(key < mylist[middle]):
        upper = middle - 1
        recursivebinary(key,low,upper)
    elif(key > mylist[middle]):
        low = middle + 1
        recursivebinary(key,low,upper)

        
    

    
    
    
def binary_search(searchlist,key):
    
    length = len(searchlist)
    
    low = 0
    upper = length - 1
    
    while(low <= upper):
        middle = (low + upper) // 2
        
        if (key == searchlist[middle]):
            return middle
        
        elif (key < searchlist[middle]):
            upper = middle -1
        
        elif (key > searchlist[middle]):
            low = middle +1
        
    return False


print(timeit.timeit('recursivebinary(78,0,len(mylist)-1)',setup='from __main__ import recursivebinary',globals=globals()))


'''st = time.time()
print(binary_search(mylist,78))
en = time.time()
print('Time Module time ', en-st)

print(timeit.timeit('x=10'))
input()

print(timeit.timeit('binary_search(mylist,78)',setup='from __main__ import binary_search' ,globals=globals()))'''


#print(binary_search(mylist,100))
    
    