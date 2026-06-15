from typing import Optional

head = [1]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(values):
    dummy = ListNode()
    current = dummy

    for val in values:
        current.next = ListNode(val)
        current = current.next

    return dummy.next

LinkedList = build_linked_list(head)


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        current = head
        counter = 0
        while current is not None:
            counter += 1
            current = current.next
        counter = counter // 2
        print(counter)
        current = head
        for i in range(counter - 1):
            current = current.next
        current.next = current.next.next
        return head
        

def printList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

print("Before deletion:")
printList(LinkedList)

solution = Solution()
result = solution.deleteMiddle(LinkedList)

print("After deletion:")
printList(result)