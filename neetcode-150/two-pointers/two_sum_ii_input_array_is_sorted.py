"""
Submission Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/1675353032
"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers)-1
        
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s > target:
                r -= 1
            else:
                l += 1
        
        return [-1, -1]
