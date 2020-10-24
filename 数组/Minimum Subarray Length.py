class Solution(object):
  def minSubArray(self, k, nums):
    leftIndex = rightIndex = 0
    sum = 0
    minLen = float('inf')

    while rightIndex < len(nums):
      sum += nums[rightIndex]
      while sum >= k:
        minLen = min(minLen, rightIndex - leftIndex + 1)
        sum -= nums[leftIndex]
        leftIndex += 1
      rightIndex += 1

    if minLen == float('inf'):
      return 0
    return minLen

print(Solution().minSubArray(7, [2, 3, 1, 2, 4, 3]))
# 2