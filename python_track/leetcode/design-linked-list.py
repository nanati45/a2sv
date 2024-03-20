class Doubly:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = Doubly(0)
        self.tail = Doubly(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.tail and index == 0 :
            return curr.val      
        return -1

    def addAtHead(self, val: int) -> None:
        node = Doubly (val)
        prev_ , next_ = self.head , self.head.next
        prev_.next = node
        node.prev = prev_
        node.next = next_
        next_.prev = node

    def addAtTail(self, val: int) -> None:
        node = Doubly (val)
        prev_ , next_ = self.tail.prev , self.tail
        prev_.next = node
        node.prev = prev_
        node.next = next_
        next_.prev = node

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.next
        while curr and index > 0 :
            curr = curr.next
            index -= 1
        if curr and index == 0 :
            node = Doubly (val)
            prev_ , next_ = curr.prev , curr
            prev_.next = node
            node.prev = prev_
            node.next = next_
            next_.prev = node    

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next
        while curr and index > 0 :
            curr = curr.next
            index -= 1
        if curr and curr != self.tail and index == 0 :
            prev_ , next_ = curr.prev , curr.next
            prev_.next = next_
            next_.prev = prev_
            
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)