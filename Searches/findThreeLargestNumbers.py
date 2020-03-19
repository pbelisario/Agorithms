def findThreeLargestNumbers(array):
    largest_numbers = [float('-inf'), float('-inf'), float('-inf')]

    for number in array:
        if number > largest_numbers[2]:
            largest_numbers[0] = largest_numbers[1]
            largest_numbers[1] = largest_numbers[2]
            largest_numbers[2] = number
        elif number > largest_numbers[1]:
            largest_numbers[0] = largest_numbers[1]
            largest_numbers[1] = number
        elif number > largest_numbers[0]:
            largest_numbers[0] = number
    return largest_numbers

print(findThreeLargestNumbers([2,5,48,6,52,10,9,7]))