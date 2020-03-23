'''
    Return an array of the starting and ending indices of the smallest subarray
     in the input array that needs to be sorted in place in order 
     for the entire input array to be sorted
'''
def subArraySort(array):
    minOutOrder = float('inf')
    maxOutOrder = float('-inf')

    for i in range(len(array)):
        
        num = array[i]

        if isOutOfOrder(i, num, array):
            minOutOrder = min(num, minOutOrder)
            maxOutOrder = max(num, maxOutOrder)
        
    if minOutOrder == float('inf'):
        return [-1, -1]
        
    subArrayLeftIdx = 0
    subArrayRightIdx = len(array) - 1
    while minOutOrder >= array[subArrayLeftIdx]:
        subArrayLeftIdx += 1
    while maxOutOrder <= array[subArrayRightIdx]:
        subArrayRightIdx -= 1
    return [subArrayLeftIdx, subArrayRightIdx]

def isOutOfOrder(i, num, array):
    if i == 0:
        return num > array[i+1]
    if i == len(array) - 1:
        return num < array[i-1]
    return num > array[i+1] or num < array[i-1]

print(subArraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19] ))