# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        oddHead = ListNode()
        oddTail = ListNode()
        evenHead = ListNode()
        evenTail = ListNode()
        odd = True
        pointHead = ListNode()
        pointHead.next = head
        while pointHead.next:
            if odd:
                if not oddHead.next:
                    oddHead.next = pointHead.next
                oddTail.next = pointHead.next
                pointHead.next = pointHead.next.next
                oddTail = oddTail.next
                oddTail.next = None
                odd = False
            else:
                if not evenHead.next:
                    evenHead.next = pointHead.next
                evenTail.next = pointHead.next
                pointHead.next = pointHead.next.next
                evenTail = evenTail.next
                evenTail.next = None
                odd = True
        oddTail.next = evenHead.next
        return oddHead.next