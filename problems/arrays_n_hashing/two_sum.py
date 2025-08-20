from typing import List

# [Hash Map (One Pass)]
# Time: O(n) | Space: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i 


# # [1. Brute Force Approach]
# # Time: O(n^2) | Space: O(1)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return []

# # [2. Sorting + Two pointer Approach]
# # Time: O(nlogn) | Space: O(n)
# class Solution:
#     def twoSum(self, nums:List[int], target: int) -> List[int]:
#         # We sort the array after storing original positions
#         A = [[num, i] for i, num in enumerate(nums)]
#         A.sort()

#         # Add items at extremes of list and adjust index to find target
#         i = 0; j = len(nums) - 1
#         while i < j:
#             cur = A[i][0] + A[j][0]
#             if cur == target:
#                 # Return the first combination we would have gotten for sum
#                 return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]
#             elif cur < target:
#                 i += 1
#             else:
#                 j -= 1
#         return []

# # [3. Hash Map (Two Pass)]
# # Time: O(n) | Space: O(n)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         # Store all indices of each number in dictionary
#         hash_indices = {n:i for i,n in enumerate(nums)}

#         # Find if difference required for each num has its index stored
#         for i, n in enumerate(nums):
#             diff = target - n
#             if diff in hash_indices and hash_indices[diff] != i:
#                 return [i, hash_indices[diff]]