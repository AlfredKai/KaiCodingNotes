from math import floor

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        a = []
        while head != None:
            a.append(head.val)
            head = head.next
        for i in range(0, floor(len(a) / 2)):
            if a[i] != a[-(i + 1)]:
                return False
        
        return True

b = ListNode(1)
b.next = ListNode(2)
b.next.next = ListNode(3)
b.next.next.next = ListNode(4)

a = Solution()
print(a.isPalindrome(b))

b = ListNode(1)
b.next = ListNode(2)
b.next.next = ListNode(2)
b.next.next.next = ListNode(1)

a = Solution()
print(a.isPalindrome(b))