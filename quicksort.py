from threading import Thread
import threading
import time



def qsort(list,left,right):

    i = left
    j = right
    pivot = list[(left + right)//2]
    temp = 0
    while(i <= j):
         while(pivot > list[i]):
             i = i+1
         while(pivot < list[j]):
             j = j-1
         if(i <= j):
             temp = list[i]     
             list[i] = list[j]
             list[j] = temp
             i = i + 1
             j = j - 1

    lthread = None
    rthread = None

    if (left < j):
        lthread = Thread(target = lambda: qsort(list,left,j))
        lthread.start()

    if (i < right):
        rthread = Thread(target=lambda: qsort(list,i,right))
        rthread.start()

    if lthread is not None: lthread.join()
    if rthread is not None: rthread.join()
    return list


# Function to find the partition position
def partition(array, low, high):

	# choose the rightmost element as pivot
	pivot = array[high]

	# pointer for greater element
	i = low - 1

	# traverse through all elements
	# compare each element with pivot
	for j in range(low, high):
		if array[j] <= pivot:

			# If element smaller than pivot is found
			# swap it with the greater element pointed by i
			i = i + 1

			# Swapping element at i with element at j
			(array[i], array[j]) = (array[j], array[i])

	# Swap the pivot element with the greater element specified by i
	(array[i + 1], array[high]) = (array[high], array[i + 1])

	# Return the position from where partition is done
	return i + 1

# function to perform quicksort


def quickSort(array, low, high):
	if low < high:

		# Find pivot element such that
		# element smaller than pivot are on the left
		# element greater than pivot are on the right
		pi = partition(array, low, high)

		# Recursive call on the left of pivot
		quickSort(array, low, pi - 1)

		# Recursive call on the right of pivot
		quickSort(array, pi + 1, high)


lst = [i for i in range(500)]



size = len(lst)
x=time.time()
print(x)
quickSort(lst, 0, size - 1)
y=time.time()
print(y)
print('normal quicksort')
print((y-x)*1000)
res1=y-x


x=time.time()
print(x)
res = qsort(lst, 0, len(lst) - 1)
y=time.time()
print(y)
print("thread",(y-x)*1000)
res2=y-x

print(res2-res1)




