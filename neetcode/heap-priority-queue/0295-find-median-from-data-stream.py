import heapq


class MedianFinder:
    def __init__(self):
        # What we want to do is to divide the stream of data coming in,
        # into two halves:
        #
        #   - a `low` side implemented with a max-heap (using negated min-heap operations).
        #   - a `high` side implemented with a min-heap.
        #
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        # We're biased towards inserting into the `low` side
        # as do so when it is empty or whenever a value comes
        # in that is less than its current maximum value.
        side = "low" if len(self.low) == 0 or num < -self.low[0] else "high"

        match side:
            case "low":
                # We implement a max-heap for `low` by negating values
                # that are passed into a min-heap causing large values
                # to act like large negative values (minimum values).
                heapq.heappush(self.low, -num)
            case "high":
                heapq.heappush(self.high, num)

        # We need to ensure that the length of the heaps are balanced
        # such that either the `low` side is the same length as the
        # `high` side or it is one greater than this (if there are an
        # odd number of elements and the median is found as the `max`
        # value at the root of the `low` heap).
        #
        # An example of how we could end up with unbalanced heaps would
        # be if the numbers inserted were descending and all ended up
        # within `low` with nothing in `high`.
        self._balance_heaps()

    def _balance_heaps(self):
        if len(self.low) > len(self.high) + 1:
            # If the `low` max-heap is more than one-element longer
            # than the `high` min-heap we need to pop the max value
            # from this heap and place it into `high`.
            #
            # Note: in this situation we're negating as we stored
            #       negated values in a min-heap to convert it into
            #       a max-heap, and need to get back the original value.
            heapq.heappush(self.high, -heapq.heappop(self.low))
        elif len(self.high) > len(self.low):
            # If the `high` min-heap has more elements than the
            # `low` max-heap we need to pop the min value
            # from this heap and place it into `low`.
            #
            # Note: in this situation we're negating before we insert
            #       into `low` as this is how we make a min-heap behave
            #       as a max-heap.
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        is_odd_length = (len(self.low) + len(self.high)) % 2 != 0
        if is_odd_length:
            midpoint = -self.low[0]
            return midpoint
        else:
            max_of_low, min_of_high = -self.low[0], self.high[0]
            return (max_of_low + min_of_high) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
