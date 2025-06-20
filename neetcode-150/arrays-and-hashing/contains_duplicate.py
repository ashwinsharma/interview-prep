"""
Submission Link: https://leetcode.com/problems/contains-duplicate/submissions/1670877792
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()
        for n in nums:
            if n in s:
                return True
            else:
                s.add(n)
        return False