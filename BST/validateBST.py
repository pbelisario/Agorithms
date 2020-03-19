def validateBST(tree):
    return treeHelper(tree, float('-inf'), float('inf'))

def treeHelper(tree, min_Value, max_Value):
    if tree is None:
        return True
    elif tree.value < min_Value or tree.value >= max_Value:
        return False
    elif tree.left and tree.value < tree.left.value:
        return False
    elif tree.right and tree.value > tree.right.value:
        return False
    else:
        return treeHelper(tree.left, min_Value, tree.value) and treeHelper(tree.right, tree.value, max_Value)