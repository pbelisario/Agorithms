'''
    Returns an array of length 2 representing the largest range of numbers contained in that array
    The first number in the output array should be the first number in the range
    The second number should be the last number in the range
    A range of numbers is dened as a set of numbers that come right after each other in the set of real integers
    Numbers do not need to be ordered or adjacent in the array in order to form a range. 
    Assuming that there will only be one largest range
'''

def largestRange(array):
    bestRange = []
    longestRange = 0
    nums = {}

    for num in array:
        nums[num] = True
    for num in array:
        if not nums[num]:
            continue
        nums[num] = False
        currentLenght = 1
        left = num - 1
        right = num + 1
        while left in nums:
            nums[left] = False
            currentLenght += 1
            left -= 1
        while right in nums:
            nums[right] = False
            currentLenght += 1
            right += 1
        if currentLenght > longestRange:
            longestRange  = currentLenght
            bestRange = [left + 1, right - 1]
    return bestRange

print(largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))