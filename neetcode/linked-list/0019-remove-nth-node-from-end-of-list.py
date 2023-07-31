from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # If we were doing this in two-passes, in the first-pass we would get the length `L`
        # of the linked list and then use a second pass to skip the node `L - n` from the
        # end.
        #
        # However, if we want to do this in one pass only, we will have to take a different
        # approach that is much more demented.
        if head.next is None:
            return None

        # We want to move forwards up to the nth index, ensuring that
        # `headLessN` points to a linked list that is `L - n` long.
        #
        # This is useful because we can then iterate through this linked
        # list while setting up a new linked list up to this point, before
        # eventually skipping the node at `L - n` by pointing `.next` to
        # `.next.next`.
        headLessN = head
        for i in range(n + 1):
            headLessN = headLessN.next
            # We special-case the situations in which we consume
            # all of `head` counting up to `n` and if we've
            # counted to `n - 1` return the head without its first
            # element.
            #
            # Note: it's not possible for n to be greater than the
            #       length of the linked list within the test cases.
            if not headLessN and i == n - 1:
                return head.next

        current = head
        newHead = current
        while headLessN:
            current = current.next
            headLessN = headLessN.next

        current.next = current.next.next

        return newHead
