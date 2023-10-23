from typing import List
import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # It's possible to capture the k largest elements within
        # a min-heap if you ensure that you replace the smallest
        # element in it with any element larger than this.
        self.min_heap = []
        for num in nums:
            self.add(num)

    def add(self, num: int) -> int:
        # When the heap has fewer than `k` elements we always
        # push an element to it.
        #
        # But once it has `k` elements we only push further elements
        # after we pop any element within it that is smaller than
        # the new element.
        #
        # This makes a heap invariant that:
        # (1) The min-heap is actually the set of k largest elements
        #     seen so far.
        # (2) The 0th element is the kth largest element.
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, num)
        elif self.min_heap[0] < num:
            heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, num)
        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
