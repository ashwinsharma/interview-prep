"""
Submission Link: https://leetcode.com/problems/top-k-frequent-elements/submissions/1670950649
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        fd = {}
        
        for n in nums:
            fd[n] = fd.get(n, 0) + 1
        
        nums_desc_freq = [n for n, _ in sorted(fd.items(), reverse=True, key=lambda x: x[1])]

        return nums_desc_freq[:k]
