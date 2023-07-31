from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None

        # We want to operate upon the list with the lowest prefix.
        a, b = (
            (list1, list2)
            if getattr(list1, "val", float("inf"))
            <= getattr(list2, "val", float("inf"))
            else (list2, list1)
        )

        current = ListNode(a.val)
        a = a.next

        head = current
        while a is not None and b is not None:
            if a.val <= b.val:
                current.next = ListNode(a.val)
                a = a.next
            else:
                current.next = ListNode(b.val)
                b = b.next

            current = current.next

        remaining = a if a is not None else b
        while remaining is not None:
            current.next = ListNode(remaining.val)
            remaining = remaining.next
            current = current.next

        return head
