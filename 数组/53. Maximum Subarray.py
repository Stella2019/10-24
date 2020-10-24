"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums) < 0:
            return max(nums)
        local_max, global_max = 0, 0
        for num in nums:
            local_max = max(0, local_max + num)
            global_max = max(global_max, local_max)
        return global_max




class Solution:
  def maxSubArray(self, nums):
    maxSum = 0
    sum = 0
    for n in nums:
      sum += n
      if sum < 0:
        sum = 0
      else:
        maxSum = max(maxSum, sum)
    return maxSum

print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# 6

print(Solution().maxSubArray([-1, -4, 3, 8, 1]))
# 12