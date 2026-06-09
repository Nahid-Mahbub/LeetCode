# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class Solution:
    def insertGreatestCommonDivisors(self, head):
        current = head

        while current and current.next:
            g = gcd(current.val, current.next.val)
            newNode = ListNode(g)

            newNode.next = current.next
            current.next = newNode
            current = newNode.next
        return head
def printList(head):
    current = head
    while current:
        print(current.val, end = "->")
        current = current.next
    print("None")

head = ListNode(18)
head.next = ListNode(6)
head.next.next = ListNode(10)
head.next.next.next = ListNode(3)

solution = Solution()
result = solution.insertGreatestCommonDivisors(head)
printList(result)