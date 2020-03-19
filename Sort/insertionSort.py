def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while array[j] < array[j-1] and j > 0:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
    return array


print(insertionSort([2,5,4,1,14,6,3,0,78,9]))