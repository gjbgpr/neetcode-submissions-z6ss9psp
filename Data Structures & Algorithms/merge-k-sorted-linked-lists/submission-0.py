# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(pq, (lists[i].val, i, lists[i]))

        dummy = ListNode()
        tail = dummy

        while pq:
            value, index, node = heapq.heappop(pq)

            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(pq, (node.next.val, index, node.next))

        return dummy.next