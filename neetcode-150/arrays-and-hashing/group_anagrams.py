"""
Submission Link: https://leetcode.com/problems/group-anagrams/submissions/1670941133
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in d:
                d[sorted_s] = []
            d[sorted_s].append(s)
        
        return list(d.values())
