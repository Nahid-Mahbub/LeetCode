# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        linklist = l1
        linklist2 = l2
        list1 = []
        list2 = []
        printList(linklist)
        printList(linklist2)
        while linklist:
            list1.append(linklist.val)
            linklist = linklist.next
        while linklist2:
            list2.append(linklist2.val)
            linklist2 = linklist2.next
        print(list1, list2)
        list1 = list1[::-1]
        list2 = list2[::-1]
        print(list1, list2)
        num1 = int("".join(map(str, list1)))
        num2 = int("".join(map(str, list2)))
        print(num1, num2)
        total = num1 + num2
        print(total)
        total_list = list(str(total))
        total_list = total_list[::-1]
        print(total_list)
        dummy = ListNode()
        curr = dummy
        for x in total_list:
            curr.next = ListNode(int(x))
            curr = curr.next
        return dummy.next

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


list1 = helper([9,9,9,9,9,9,9])
list2 = helper([9,9,9,9])
solution = Solution()
result = solution.addTwoNumbers(list1, list2)
printList(result)