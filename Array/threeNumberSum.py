def threeNumberSum (array, targetSum):
    sumList = []

    array.sort()

    for x in range(len(array)-2):
        
        j = x+1
        k = len(array) - 1

        while j < k:
            if array[x] + array[j] + array[k] == targetSum:
                # if the combination was found,
                # move j and k over,
                sumList.append([array[x], array[j], array[k]])
                j += 1
                k -= 1
            elif array[x] + array[j] + array[k] < targetSum:
                # Go check higher numbers for left pointers
                j += 1
            else:
                # Go check lower numbers for right pointers
                k -= 1
    return sumList

print (threeNumberSum([2,2,2, 3, 6, 1, 5, 4], 7 ))

