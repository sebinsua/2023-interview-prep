from typing import Optional

import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Note: this is my first solution, but it can be made faster through the use of a
    #       priority queue (e.g. heapq).
    def mergeKListsSlow(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        _dummy = ListNode(-1)

        merged_list = _dummy
        current = merged_list
        while True:
            smallest_val = float("inf")
            selected_index = -1
            for index, lst in enumerate(lists):
                if lst and lst.val < smallest_val:
                    smallest_val = lst.val
                    selected_list = lst
                    selected_index = index

            # Once we've finished sorting it'll be impossible to find
            # any lists that still contain elements that can be consumed.
            if selected_index == -1:
                break

            # Add the value found within the list we selected and then
            # point current towards the next element.
            current.next = ListNode(lists[selected_index].val)
            current = current.next

            # Skip the first element within a selected list as it is consumed.
            lists[selected_index] = lists[selected_index].next

        # We remove the dummy element by skipping it with `.next`.
        return merged_list.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        # We populate a min-heap with the first element of each list (consuming it as we do).
        for index in range(len(lists)):
            if lists[index] is not None:
                heapq.heappush(min_heap, (lists[index].val, index))
                lists[index] = lists[index].next

        # We create the linked list we intend to merge into.
        _dummy = ListNode(-1)
        merged_list = _dummy

        current = merged_list
        # While there are elements in linked lists we've still not consumed
        # and that populate our min-heap, we iterate popping the minimum
        # from this heap, where we've stored its value and related list index.
        while len(min_heap) > 0:
            smallest_val, selected_index = heapq.heappop(min_heap)

            # Add the minimum value to the end of our `merged_list` and then point
            # the `current` pointer at this next element.
            current.next = ListNode(smallest_val)
            current = current.next

            # Whenever a minimum value from the heap is used, we need to ensure that
            # another element (if it exists) is added from that list, and that we
            # consume the element that was just used.
            if lists[selected_index] is not None:
                heapq.heappush(min_heap, (lists[selected_index].val, selected_index))
                lists[selected_index] = lists[selected_index].next

        # We remove the dummy element by skipping it with `.next`.
        return merged_list.next
