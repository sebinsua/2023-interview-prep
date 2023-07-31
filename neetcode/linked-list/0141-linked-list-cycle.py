from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # We'll use Floyd's Cycle Finding Algorithm which uses two pointers:
        # a slow one and a fast one and then returns `True` if they ever touch
        # and `False` otherwise.
        #
        # This is instead of needing to store every visited `Node` in a `set`
        # and checking for existence within this, which potentially could use
        # a lot of memory if there is no cycle or a very large cycle.
        slow_pointer = head
        fast_pointer = head
        while slow_pointer and fast_pointer:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next if fast_pointer.next else None
            if not slow_pointer or not fast_pointer:
                break

            if slow_pointer is fast_pointer:
                return True

        return False
