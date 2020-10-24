# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        p = dummy = ListNode(-1)
        for i in xrange(0, len(lists)):
            node = lists[i]
            if not node:
                continue
            heapq.heappush(heap, (node.val, node))

        while heap:
            value, node = heapq.heappop(heap)
            p.next = node
            p = p.next
            if node.next:
                node = node.next
                heapq.heappush(heap, (node.val, node))
        return dummy.next