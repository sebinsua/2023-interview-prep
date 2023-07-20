from typing import List
import heapq


def find_min_paths(g: List[List[int]], start: int) -> List[int]:
    # Initialize the distances list: distances[i] is the minimum distance from the
    # start vertex to vertex i. Set the distance to the start vertex as 0 and
    # all other vertices as infinity.
    distances = [float("inf")] * len(g)
    distances[start] = 0

    # Initialize the priority queue with the distance (0) to the start vertex.
    queue: List[Tuple[int, int]] = [(0, start)]  # (distance, node)

    # Dijkstra's algorithm.
    #
    # We continue to loop while there are nodes reachable from `start` that are
    # yet to be processed. We keep on adding neighbours to this queue while doing
    # so results in distances smaller than already known for each neighbour.
    #
    # Once we've found minimum distances items are no longer added to the queue
    # which ends up getting emptied by `.heappop`.
    while queue:
        # Get the node with the current minimum distance.
        current_minimum_distance, current_node_index = heapq.heappop(queue)

        # As an optimization, we skip processing the neighbours of a node with a distance
        # that is strictly greater than the distance computed to the `current_node_index`.
        # This could happen if an earlier iteration has already updated `distances[i]` with
        # a smaller minimum distance after we had added a particular neighbour to the
        # priority queue.
        #
        # Note that, if the distance is equal we still want to check the neighbours of the
        # current node, in order to explore and find new paths that might offer shorter
        # distances.
        if current_minimum_distance > distances[current_node_index]:
            continue

        # Loop through the current node's neighbours.
        for neighbour_index, neighbour_weight in enumerate(g[current_node_index]):
            # Skip a neighbour if there is no edge from `current_node_index` to `neighbour_index`.
            if neighbour_weight == -1:
                continue

            previous_distance_to_neighbour = distances[neighbour_index]
            new_distance_to_neighbour = current_minimum_distance + neighbour_weight

            # For each neighbour of the current node we ensure that `distances[i]` is minimized by
            # comparing each new distance to the one we've already stored.
            distances[neighbour_index] = min(
                previous_distance_to_neighbour, new_distance_to_neighbour
            )

            # If the neighbour of the current node has a smaller distance from `start` to itself
            # compared to other paths we've already considered, we'll add it to the priority queue
            # so we can consider its own neighbours in a future iteration of the while loop.
            #
            # Important: eventually once we've found the minimum distance to each vertex, this if-block
            #            will stop finding new nodes to push onto the priority queue and the algorithm
            #            will begin to
            if new_distance_to_neighbour < previous_distance_to_neighbour:
                heapq.heappush(queue, (new_distance_to_neighbour, neighbour_index))

    # Return the shortest distances from the `start` to all vertices.
    return distances


def solution(g: List[List[int]], s: int) -> List[int]:
    return find_min_paths(g, s)
