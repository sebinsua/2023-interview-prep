from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return head

        # Deep copy and reverse the linked list.
        previous = None
        current = head
        L = 0
        while current:
            new_node = ListNode(current.val)
            new_node.next = previous

            previous = new_node

            current = current.next

            L += 1

        reversed_head = previous
        is_even = L % 2 == 0

        # Merge the two linked lists alternately.
        n = 0
        while head and reversed_head:
            previous_next_head = head.next
            previous_reversed_head = reversed_head.next
            head.next = reversed_head
            head.next.next = previous_next_head

            n += 2
            if is_even and n == L:
                reversed_head.next = None
                break

            if not is_even and n + 1 == L:
                reversed_head.next.next = None
                break

            head = previous_next_head
            reversed_head = previous_reversed_head

        # I am told that a better way of solving this problem is to:
        # 1. Use two-pointers which will set the `slow` pointer to the midpoint
        #    once `fast` reaches the end of the linked list.
        #
        #    e.g.
        #
        #    slow = fast = head
        #    while slow and fast.next:
        #        slow = slow.next
        #        fast = fast.next.next
        #
        # 2. Take the `slow` pointer and then reverse the rest of its nodes.
        #    Take a pointer to its last node and call this `reversed_last_half`.
        #
        #    e.g.
        #
        #    second_half_start = slow.next
        #    previous = None
        #    while second_half_start:
        #        next_node = second_half_start.next
        #        second_half_start.next = previous
        #        previous = second_half_start
        #        second_half_start = next_node
        #
        # 3. Merge the two halves: `first_half (`head`) and `reversed_last_half`
        #    by alternatively connecting them while `reversed_last_half` is not `None`.
        #
        #    Note: `first_half` is severed from the rest of the linked list earlier using:
        #
        #    slow.next = None
        #
        #    And then merged with:
        #
        #    first_half, second_half = head, prev
        #    while second_half:
        #        tmp = first_half.next
        #        first_half.next = second_half
        #        first_half = tmp
        #
        #        tmp = second_half.next
        #        second_half.next = first_half
        #        second_half = tmp
        return head
