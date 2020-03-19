def smallestDifference(array1, array2):
    array1.sort()
    array2.sort()
    
    i = 0
    j = 0
    
    first_number = array1[i]
    second_number = array2[j]

    size_arr1 = len(array1) - 1
    size_arr2 = len(array2) - 1

    min_value = float('inf')

    while first_number is not None and second_number is not None:
        if abs(first_number - second_number) == 0:
            return [first_number, second_number]
        if abs(first_number - second_number) < min_value:
            min_value = abs(first_number - second_number)
            min_arr = [first_number, second_number]
        elif first_number > second_number:
            j += 1
            if j > size_arr2:
                return min_arr
            else:
                second_number = array2[j]
        else:
            i +=1
            if i > size_arr1:
                return min_arr
            else:
                first_number = array1[i]


print(smallestDifference([2,5,4,17,6,3,78,9], [11,12,13,14,15]))