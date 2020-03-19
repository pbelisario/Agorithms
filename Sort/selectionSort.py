def selectionSort(array):
    for i in range(len(array)):
        last_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[last_index]:
                last_index = j
            array[last_index], array[i] = array[i], array[last_index]
    return array

print(selectionSort([2,5,4,1,14,6,3,0,78,9]))