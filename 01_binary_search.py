import time
import timeit

def binary_search(list, item,low,high):
  # low and high keep track of which part of the list you'll search in.
  #low = 0
  #high = len(list) - 1

  # While you haven't narrowed it down to one element ...
  while low <= high:
    # ... check the middle element
    mid = (low + high) // 2
    guess = list[mid]
    # Found the item.
    if guess == item:
      return mid
    # The guess was too high.
    if guess > item:
      high = mid - 1
    # The guess was too low.
    else:
      low = mid + 1

  # Item doesn't exist
  return None

my_list = [1, 3, 5, 7, 9,10,20,40,50,60]
st = time.time()
#print(binary_search(my_list, 20)) # => 1
en = time.time()
print('Time taken to execute ',en-st)
print(timeit.timeit('x=10'))
input()
low=0
high=len(my_list)-1
print(timeit.timeit('binary_search(my_list,1,low,high)',setup='from __main__ import binary_search' ,globals=globals()))

# 'None' means nil in Python. We use to indicate that the item wasn't found.
#print(binary_search(my_list, -1)) # => None
