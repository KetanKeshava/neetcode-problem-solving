class ListNode:
    def __init__(self, preferredSandwich):
        self.preferredSandwich = preferredSandwich
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, preferredSandwich):
        newNode = ListNode(preferredSandwich)

        if self.head is None and self.tail is None:
            self.head = newNode
            self.tail = newNode

        else:
            self.tail.next = newNode
            self.tail = newNode

        self.length += 1

    def dequeue(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None

        else:
            removeNode = self.head
            self.head = self.head.next
            removeNode.next = None

        self.length -= 1

    def getStudentPreferredSandwichAtFront(self):
        return self.head.preferredSandwich

    def getStudentsLeft(self):
        return self.length

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # circular = 0
        # square = 1

        # convert students list to a queue
        stdQueue = Queue()
        for studentPreferredSandwich in students:
            stdQueue.enqueue(studentPreferredSandwich)

        s = 0

        noMatch = False
        studentsLeft = None
        noMatchCount = 0

        while s < len(sandwiches):

            studentPreferredSandwichAtFront = stdQueue.getStudentPreferredSandwichAtFront()

            if studentPreferredSandwichAtFront == sandwiches[s]:
                s = s + 1
                stdQueue.dequeue()
                noMatch = False
                studentsLeft = None

            else: 
                stdQueue.dequeue()
                stdQueue.enqueue(studentPreferredSandwichAtFront)

                if noMatch == True:
                    if stdQueue.getStudentsLeft() == studentsLeft:
                        noMatchCount += 1

                    if noMatchCount == studentsLeft:
                        return studentsLeft

                else:
                    noMatch = True
                    studentsLeft = stdQueue.getStudentsLeft()
                    noMatchCount = 1

                    if noMatchCount == studentsLeft:
                        return studentsLeft

        return 0





                

        






        