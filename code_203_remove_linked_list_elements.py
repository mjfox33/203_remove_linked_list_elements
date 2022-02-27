# Definition for singly-linked list.
from unittest.mock import sentinel


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = worker = ListNode(0,head)
        while worker and worker.next:
            if worker.next.val == val:
                worker.next = worker.next.next
            else:
                worker = worker.next
        return sentinel.next