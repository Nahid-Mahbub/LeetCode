# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        print(node.val)
        node.val = node.next.val
        node.next = node.next.next
        print(node.val)
        

node = ListNode(5)
node.next = ListNode(1)
node.next.next = ListNode(9)

solution = Solution()
head = [4,5,1,9]
result = solution.deleteNode(node)
print(result)