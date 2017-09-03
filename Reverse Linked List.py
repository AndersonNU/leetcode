# Reverse a singly linked list.
<<<<<<< HEAD


=======
#
>>>>>>> a039542b85e72ea1389b15f131b6783507aa7e2e

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
<<<<<<< HEAD
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
=======
>>>>>>> a039542b85e72ea1389b15f131b6783507aa7e2e
