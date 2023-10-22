from typing import List
import heapq


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # We sort the intervals and queries in order that we can process them in order
        # and in lock-step. In this algorithm this is very important as it ensures that
        # the intervals are implicitly grouped by their query by maintaining a min-heap
        # that is updated on every iteration to always contain the intervals related to
        # that particular query. These groupings are potentially overlapping since
        # intervals can start before a query and end after it.
        sorted_intervals = sorted(intervals)
        sorted_queries = sorted(queries)
        i = 0

        # Heap Invariant: Maintaining intervals that have started but not yet ended as of
        #                 the current query point, sorted by their lengths.
        min_heap = []
        # We will store the results of each query in a map. At the end of the function
        # we can use this alongside the sorted queries to return the results in the
        # correct order.
        query_map = {}

        # For each query, we will (1) take all intervals that start before the query (or
        # at it) and  add them to the min-heap using the length of the interval as the key,
        # and (2) then we will pop all intervals from the min-heap that end before the query,
        # and finally (3) we will take the top of the min-heap as the answer to the query.
        for q in sorted_queries:
            # Any interval that starts before the query is a potential candidate for the
            # answer to the query.
            while i < len(sorted_intervals) and sorted_intervals[i][0] <= q:
                left, right = sorted_intervals[i]

                # Using the length of the interval as the key ensures that we have a cheap
                # way to find the smallest interval that starts before the query.
                length = right - left + 1
                heapq.heappush(min_heap, (length, left, right))

                i += 1

            # Any interval that ends before the query does not contain the query, and
            # therefore cannot be the answer to the query. We remove these candidates.
            while len(min_heap) > 0 and min_heap[0][2] < q:
                heapq.heappop(min_heap)

            # As the min-heap contains all intervals that start before the query, and
            # we've removed all of these intervals that end before the query, the top-most
            # interval in the min-heap is the smallest interval that contains the query.
            query_map[q] = min_heap[0][0] if len(min_heap) > 0 else -1

            # Note: Often the min-heap will not be empty at this point, and will in fact
            #       contain intervals that started before the query but have not yet ended.
            #       This is fine -- these intervals are candidate minimum intervals for
            #       future queries.

        # Finally, we return the results in the order of the queries.
        return [query_map[q] for q in queries]
