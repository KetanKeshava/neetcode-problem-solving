class ListNode:
    def __init__(self, val = None):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        
        curr = self.head
        for _ in range(index):
            curr = curr.next

        return curr.val

    def addAtHead(self, val: int) -> None:
        new = ListNode(val)

        if self.head is None and self.tail is None:
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head = new

        self.length += 1
        
    def addAtTail(self, val: int) -> None:
        new = ListNode(val)
        if self.head is None and self.tail is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new

        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        elif index > self.length:
            return
        else:
            new = ListNode(val)

            curr = self.head
            prev = None
            for _ in range(index):
                prev = curr
                curr = curr.next

            prev.next = new
            new.next = curr
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            remove = self.head
            self.head = head.next
            remove.next = None
            self.length -= 1
        
        elif index >= self.length:
            return

        else:
            curr = self.head
            prev = None
            for _ in range(index):
                prev = curr
                curr = curr.next

            if index == self.length - 1:
                prev.next = None
                self.tail = prev
            else:
                prev.next = curr.next
                curr.next = None
            self.length -= 1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)