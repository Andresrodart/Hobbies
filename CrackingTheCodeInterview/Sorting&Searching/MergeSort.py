def mergeSort(arr):
	return _mergeSort(arr, [0] * len(arr), 0, len(arr) - 1)
def _mergeSort(arr, aux, leftSide, rightSide):
	if leftSide >= rightSide: return 0
	middle = (leftSide + rightSide) // 2
	return _mergeSort(arr, aux, leftSide, middle) + _mergeSort(arr, aux, middle + 1, rightSide) + merge(arr, aux, leftSide, middle, rightSide)

def merge(arr, aux, leftSide, middle, rightSide):
	for i in range(leftSide, rightSide + 1): aux[i] = arr[i]
	rightStart, leftStart = middle + 1, leftSide
	count, index = 0, leftSide
	while leftStart <= middle and rightStart <= rightSide:
		if aux[rightStart] < aux[leftStart]: 
			arr[index] = aux[rightStart]
			count, rightStart = count + (middle - leftStart) + 1, rightStart + 1
		else:
			arr[index] = aux[leftStart]
			leftStart +=  1
		index += 1
	for i in range(middle - leftStart + 1): arr[index + i] = aux[leftStart + i]
	return count

arr = [2, 1, 3, 1, 2]
print(mergeSort(arr), arr)