from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head.next
        dummy = ListNode(0)
        dummyHead = dummy
        
        counter = 0
        while current is not None:
            if (current.val == 0):
                dummyHead.next = ListNode(counter)
                dummyHead = dummyHead.next
                counter = 0
            else:
                counter += current.val
            current = current.next
        return dummy.next

def printList(head):
    current = head
    while current:
        print(current.val, end = " -> ")
        current = current.next
    print("None")

head = ListNode(0)
head.next = ListNode(3)
head.next.next = ListNode(1)
head.next.next.next = ListNode(0)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(2)
head.next.next.next.next.next.next.next = ListNode(0)

solution = Solution()
result = solution.mergeNodes(head)
printList(result)
