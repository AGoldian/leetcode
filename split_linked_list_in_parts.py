# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from math import ceil
from typing import List, Optional
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        q = k
        result = []
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        
        tmp_count = 0
        cur = head
        tmp_head = ListNode()
        tmp_iter = tmp_head
        while cur:
            tmp_count += 1

            if tmp_count == ceil(count / k):
                tmp_iter.next = ListNode(cur.val)
                tmp_count = 0
                result.append(tmp_head.next)
                count -= ceil(count / k)
                k -= 1
                tmp_head = ListNode()
                tmp_iter = tmp_head
            else:
                tmp_iter.next = ListNode(cur.val)
                tmp_iter = tmp_iter.next

            cur = cur.next
            

        
        for _ in range(q-len(result)):
            result.append(None)

        return result