"""
Submission Link: https://leetcode.com/problems/permutation-in-string/submissions/1677874773
Approach: Sliding window + hashmap where hashmap is generated from scratch for each substring of s2
"""

class Solution:
    def getFd(self, s: str) -> dict:
        fd = {}
        for c in s:
            fd[c] = fd.get(c, 0) + 1
        return fd

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_fd = self.getFd(s1)
        start, end = 0, len(s1)

        while end <= len(s2):
            fd = self.getFd(s2[start:end])
            if fd == s1_fd:
                return True
            else:
                start += 1
                end += 1
        
        return False

"""
Submission Link: https://leetcode.com/problems/permutation-in-string/submissions/1677883987
Approach: Sliding window + hashmap where hashmap is only updated as the sliding window moves along
"""

class Solution:
    def getFd(self, s: str) -> dict:
        fd = {}
        for c in s:
            fd[c] = fd.get(c, 0) + 1
        return fd

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_fd = self.getFd(s1)
        start, end = 0, len(s1) - 1
        s2_substring_fd = self.getFd(s2[start:end+1])

        while end < len(s2):
            if s2_substring_fd == s1_fd:
                return True
            else:
                s2_substring_fd[s2[start]] -= 1
                if s2_substring_fd[s2[start]] == 0:
                    s2_substring_fd.pop(s2[start])
                start += 1
                end += 1
                if end >= len(s2):
                    break
                s2_substring_fd[s2[end]] = s2_substring_fd.get(s2[end], 0) + 1
        
        return False
