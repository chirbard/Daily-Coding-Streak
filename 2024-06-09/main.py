# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # using two pointers
        # move one pointer until we have correct length.
        # if we find the end then the list isn't long enough
        # then move both pointers the same speed.
        # if we reach the end then remove left node.
        # we also have to keep track of the node before left. to modify the pointer.
        left, right = head, head
        for i in range(n - 1):
            right = right.next
        
        # our list is length of 1
        if right == head and n != 1: return right.next

        # right is at end so we have to remove first node
        if not right.next: return head.next

        right = right.next
        while right.next:
            right = right.next
            left = left.next
        
        left.next = left.next.next
        

        return head
