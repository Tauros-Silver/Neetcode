from typing import List

# [Sacrificing Space for Time]
# Time: O(n) | Space: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

# # [1. Brute Force Approach]
# # Time: O(n^2) | Space: O(1)
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         for i in range(0, len(nums)):
#             for j in range(0, len(nums)):
#                 if nums[i] == nums[j] and i != j:
#                     return True
#         return False

# # [2. Slightly better by Sorting]
# # Time: O(nlogn) | Space: O(1)
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         sorted_nums = sorted(nums)
#         temp = sorted_nums[0]
#         for i in range(1, len(nums)):
#             if sorted_nums[i] == temp:
#                 return True
#             temp = sorted_nums[i]
#         return False


# # [3. Using Set Having no duplicates]
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         if len(nums) == len(set(nums)):
#             return False
#         else:
#             return True