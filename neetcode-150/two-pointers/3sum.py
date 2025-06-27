"""
Submission Link: https://leetcode.com/problems/3sum/submissions/1678524639

Came up with solution after watching neetcode video. Slightly  differrent than the solution shown in video.
Instead of eliminating duplicates in result set in the nested while loop, I simply use a set() which will
not allow duplicate triplets to be inserted.
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = set()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            l, r = i+1, len(nums)-1
            while l < r:
                s = a + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    res.add((a, nums[l], nums[r]))
                    l += 1
            
        res = [list(x) for x in res]
        return res
