#def _init_(self, x):
 #   self.val = x
 #    self.next = None

class Solution:
    def detecCycle(selfself, head:ListNode) -> ListNode:
        fast, slow = head, head
        while fast != None:
            fast = fast.next
            if fast == None:
                break
            fast = fast.next
            slow = slow.next
            if slow == fast:
                break
        if fast == None:
            return None
        p1, p2 = slow, head
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1