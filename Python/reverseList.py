from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev


# Helper function
def helper(arr):
    dummy = ListNode()
    curr = dummy

    for value in arr:
        curr.next = ListNode(value)
        curr = curr.next

    return dummy.next


# Print function
def printList(head):
    while head:
        print(head.val, end="")
        if head.next:
            print(" -> ", end="")
        head = head.next
    print()


# ---------------- TEST ----------------

head = helper([10, 1, 13, 6, 9, 5])

print("Original List:")
printList(head)

solution = Solution()
new_head = solution.reverseList(head)

print("Reversed List:")
printList(new_head)