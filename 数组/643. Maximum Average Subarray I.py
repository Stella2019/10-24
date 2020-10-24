"""
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
"""

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        tmp = 0
        result = float('-inf')

        for i, x in enumerate(nums):
            tmp += x
            if i >= k:
                tmp -= nums[i - k]
            if i >= k - 1:
                result = max(result, tmp)
        result = result / k
        return result