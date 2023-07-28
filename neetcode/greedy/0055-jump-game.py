from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, jump in enumerate(nums):
            # If we reach an index that is higher than we could have jumped to it is unreachable
            # and therefore it would be impossible to reach the last index.
            if i > max_reach:
                return False
            
            # Iteratively compute the maximum reach by maximizing the `i + jump`.
            max_reach = max(max_reach, i + jump)
        
        # If we can traverse the entire array without bailing, we were able to reach the end from the start.
        return True