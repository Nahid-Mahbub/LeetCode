# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        prev = list1
        for _ in range(a - 1):
            prev = prev.next

        after = list1
        for _ in range(b+1):
            after = after.next
        
        trail = list2
        while trail.next:
            trail = trail.next

        prev.next = list2
        trail.next = after
    
        return list1
    
# Helper function
def helper(arr):
    dummy = ListNode()
    curr = dummy

    for x in arr:
        curr.next = ListNode(x)
        curr = curr.next
    return dummy.next

# Printer helper
def printList(head):
    while head:
        print(head.val, end="->")
        head = head.next
    print()

list1 = helper([10,1,13,6,9,5])
list2 = helper([1000000,1000001,1000002])
a = 3
b = 4
solution = Solution()
result = solution.mergeInBetween(list1, a, b, list2)
printList(list1)
