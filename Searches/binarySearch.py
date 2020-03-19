def binarySearch(array, target):
    return binaryHelper(array, target, 0, len(array)-1)

def binaryHelper(array, target, left, right):
    '''
        1 - Divide the array in half in each iteration
        2 - Look if the term in the middle is te target
        3 - If the term is bigger than the target go left
        4 - If the term is smaller than the target go right
    '''
    while left <= right:
        middle = (left+right)//2
        if array[middle] == target:
            return middle
        elif array[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return -1