from typing import List
from collections import defaultdict

# from itertools import groupby

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         def index(string: str):
#             return "".join(sorted(string))
#         return [list(group) for key, group in groupby(sorted(strs, key=index), index)]


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def key(s: str):
            return tuple(sorted(s))

        anagrams = defaultdict(list)
        for s in strs:
            anagrams[key(s)].append(s)

        return list(anagrams.values())
