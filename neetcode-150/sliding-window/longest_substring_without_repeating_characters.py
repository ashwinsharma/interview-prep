"""
Submission Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1677681488
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        start, end = 0, 0
        seen = set()
        
        while end < len(s):
            c = s[end]
            if c in seen:
                length = end - start
                max_length = max(max_length, length)
                while s[start] != c:
                    seen.remove(s[start])
                    start += 1
                start += 1
                end += 1
            else:
                seen.add(c)
                end += 1
        
        max_length = max(max_length, end - start)
        return max_length
