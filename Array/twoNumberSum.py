def twoNumberSum(array, targetSum):
    '''
        1 - Find the difference between the target sum and the current number
        2 - Store the difference in one array
        3 - If this difference is on the array, that value can be
            determined to be the second number
        3.1 - Return the two numbers sorted
        4 - Else add the difference in the array
    '''
    store_number = {None}
    for number in array:
        difference = targetSum - number
        if difference in store_number:
            return [min(number, difference), max(number, difference)]
        else:
            store_number.add(number)
    return []

print(twoNumberSum([2,1,3], 3))
print(twoNumberSum([2,1,3,4], 4))