def findClosestValueInBST:
    
    '''
        1 - Edge case of if tree is empty return None as closest node
        2 - Set initial closest value to infinite -> the first node will become closest
        3 - Iterate through tree until the Current Node is empty
            3.1 - If an empty node is reached it can be assumed that the currently
                calculated closest value must be the closest overall
        4 - Check if current node is closer to 0 difference between
            target than the closest node and if so set closest node
            to current node.
        5 - If current node value is bigger than target, go to the left branch
            Else go to the right branch
        6 - If target is equal to the closest node,
            break out of the loop and return closest node
    '''
    
    if tree in None:
        return None

    closest = float('inf')
    currentNode = tree

    while currentNode is not None:
        if abs(target - currentNode.value) < abs(target - closest)
            closest = currentNode.value
        if target < currentNode.value:
            # Go to the left branch
            currentNode = currentNode.left
        elif target > currentNode.value:
            # Go to the right branch
            currentNode = currentNode.right
        else:
            break
    return closest