"""
Submission Link: https://leetcode.com/problems/product-of-array-except-self/submissions/1671870989
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        L = [0] * n
        R = [0] * n

        L[0] = 1
        R[n-1] = 1

        for i in range(1, n):
            L[i] = L[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            R[i] = R[i+1] * nums[i+1]
        
        return [L[i] * R[i] for i in range(n)]