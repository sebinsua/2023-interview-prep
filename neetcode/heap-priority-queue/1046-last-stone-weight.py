from typing import List
import heapq


class MaxHeap:
    def __init__(self, values: List[int]):
        self.values = [-value for value in values]
        heapq.heapify(self.values)

    def __len__(self):
        return len(self.values)

    def top(self) -> int:
        return -self.values[0]

    def pop(self) -> int:
        return -heapq.heappop(self.values)

    def push(self, value: int):
        heapq.heappush(self.values, -value)


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = MaxHeap(stones)
        while len(max_heap) >= 2:
            y = max_heap.pop()
            x = max_heap.pop()
            if x != y:
                max_heap.push(y - x)

        return max_heap.top() if len(max_heap) > 0 else 0
