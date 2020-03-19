def bubbleSort(array):
    if array is None:
        return None
    bubblCheck = False

    while bubblCheck is False:
        bubblCheck = True
        for i in range(len(array)):
            try:
                if array[i] > array[i+1]:
                    array[i], array[i+1] = array[i+1], array[i] 
                    bubblCheck = False
                
            except IndexError:
                continue
    return array

print(bubbleSort([2,5,4,1,14,6,3,0,78,9]))