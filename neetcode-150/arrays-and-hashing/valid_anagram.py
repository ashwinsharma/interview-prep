"""
Submission Link: https://leetcode.com/problems/valid-anagram/submissions/1670883658
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}

        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        
        for c in t:
            if c not in d:
                return False
            else:
                d[c] -= 1
        
        for c, count in d.items():
            if count != 0:
                return False
        
        return True
