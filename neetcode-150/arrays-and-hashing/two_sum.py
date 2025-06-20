"""
Submission Link: https://leetcode.com/problems/two-sum/submissions/1670932421
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}

        for i, n in enumerate(nums):
            d[n] = i
        
        for i, n in enumerate(nums):
            if target-n in d and d[target-n] != i:
                return [i, d[target-n]]
