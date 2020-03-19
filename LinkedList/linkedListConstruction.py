class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node

        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert
    
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next

        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert


    def insertAtPosition(self, position, nodeToInsert):
        
        if position == 1:
            self.setHead(nodeToInsert)
            return
    
        currentPosition = 1
        node = self.head
        
        while currentPosition != position and node is not None:
            node = node.next
            currentPosition += 1
        
        if node is None:
            self.setTail(nodeToInsert)
        else:
            self.insertBefore(node, nodeToInsert)

    def removeNodesWithValues(self, value):
        node = self.head
        while node is not None:
            next_node = node.next
            if node.value == value:
                self.remove(node)
            node = next_node
    
    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.next = None
        node.prev = None
    
    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None
