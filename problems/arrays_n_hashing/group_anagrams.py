from collections import defaultdict
from typing import List

# [Dictionary indexed by tuple of character frequency]
# Time: O(m∗n) | Space: O(m) extra space to store distinct tuples; O(m∗n) space for the output list.
# => For m strings of length upto n
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

# # [1. Sorting based solution]
# # Time: O(m∗nlogn) | Space: O(m*n) 
# # => For m strings of length upto n
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = defaultdict(list)
#         for s in strs:
#             sortedS = ''.join(sorted(s))
#             res[sortedS].append(s)
#         return list(res.values())

# # [2. My version of tuple indexed dictionary]
# # Not as legible as when using defaultdict() but same complexities
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         groupings = {} 
#         for string in strs: 
#             char_count = [0] * 26
#             for c in string:
#                 char_count[ord(c) - ord('a')] += 1
#             str_tuple = tuple(char_count)            
#             if str_tuple not in groupings: 
#                 groupings[str_tuple] = [] 
#             groupings[str_tuple].append(string) 
#             del char_count
#         return list(groupings.values())