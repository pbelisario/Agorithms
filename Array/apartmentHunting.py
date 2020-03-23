'''
    Input: Blocks: list of blocks where each block contains an apartment that you could move into.
           Requirements: list of buildings that are important to you
    
    Output: The location (the index) of the block that is most optimal for you
    
    Objective: Minimize the farthest distance you'd have to walk 
                from your apartment to reach all of your required buildings
    
    Conditions of the Input:
        The list of blocks that you have contains information at every block 
            about all of the buildings that are present and absent at the block in question 
'''

def apartmentHunting(blocks, requirements):
    maxDistanceAtBlocks = [float('-inf') for block in blocks]
    for i in range(len(blocks)):
        for req in requirements:
            closestRegDistance = float('inf')
            for j in range(len(blocks)):
                if blocks[j][req]:
                    closestRegDistance =  min(closestRegDistance, distanceBetween(i, j))
            maxDistanceAtBlocks[i] = max(maxDistanceAtBlocks[i], closestRegDistance)
    return getIndexAtMinValue(maxDistanceAtBlocks)

def distanceBetween(i, j):
    return abs(i - j)

def getIndexAtMinValue(array):
    idxAtMinValue = 0
    minValue = float('inf')
    for i in range(len(array)):
        currentValue = array[i]
        if currentValue < minValue:
            idxAtMinValue = i
            minValue = currentValue
    return idxAtMinValue

print(apartmentHunting([ { "gym": False, "school": True, "store": False, }, { "gym": True, "school": False, "store": False, }, { "gym": True, "school": True, "store": False, }, { "gym": False, "school": True, "store": False, }, { "gym": False, "school": True, "store": True, }, ], ["gym","school","store"]))