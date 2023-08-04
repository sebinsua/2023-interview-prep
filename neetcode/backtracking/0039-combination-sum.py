from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # If there are no candidates there can be no results.
        if len(candidates) == 0:
            return []
        # If there is only one candidate, we check to see to see
        # how many elements of it can fit into the target with no
        # remainder, and if so make this the only result.
        if len(candidates) == 1 and target % candidates[0] == 0:
            return [[candidates[0]] * (target // candidates[0])]

        results = []

        # Sorting gives us further opportunities to prune the search space.
        # For example, if the smallest value in the list of candidates is
        # greater than the target, then it is impossible to find any combination
        # of numbers that equal the target.
        candidates.sort()
        if candidates[0] > target:
            return []

        # We execute a DFS using a triplet of `(index, current, total)`.
        stack = [(0, [], 0)]
        while stack:
            index, current, total = stack.pop()

            # When the total is equal to the target, it means that
            # the `current` list that we appended the last `candidate`
            # to is valid and can be added to the `results` list.
            if total == target:
                results.append(current)
                continue

            # Don't attempt to add any further candidates if the `index`
            # is already greater than the last index of `candidates`.
            if index > len(candidates) - 1:
                continue

            candidate = candidates[index]
            # If the candidate can fit into the remaining value
            # `max_times` will be non-zero. We skip adding this
            # candidate if it's too large and doesn't fit.
            max_times = (target - total) // candidate
            if max_times == 0:
                continue

            # As we know the maximum copies of a candidate that can fit, we
            # add each of these quantities of the `candidate` into the `stack`
            # while bumping the `index` in order to signify that we are ready
            # to check the next candidate.
            for times in range(max_times + 1):
                new_total = total + candidate * times

                # If the `new_total` is greater than the `target`, skip the candidate.
                if new_total > target:
                    continue

                stack.append((index + 1, current + [candidate] * times, new_total))

        return results
