# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        if head is None:
            return head

        prev = head
        head = head.next
        prev.next = None

        while head != None:
            next = head.next
            head.next = prev
            prev = head
            head = next

        return prev


class Test:
    def happyflow(self):
        # Creating a linked list with head
        # [0,1,2,3]
        node1 = ListNode(val=0,next=None)
        node2 = ListNode(val=1,next=None)
        node1.next = node2
        node3 = ListNode(val=2,next=None)
        node2.next = node3
        node4 = ListNode(val=3,next=None)
        node3.next = node4
        head = node1

        # call function that I am testing
        resultHead = Solution.reverseList() 

        # Checking if the result head is the reverse of the Linked list 
        # [3,2,1,0]

        result = [3,2,1,0]
        curr = resultHead
        for i in range(len(result)):
            if curr.val == result[i]:
                pass
            else: 
                print("Test case failed")
        print("Test case passed")








