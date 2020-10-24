class Solution(object):
  def first_missing_position(self, nums):
    hash = {}
    for n in nums:
      hash[n] = 1

    for i in range(1, len(nums)):
      if i not in hash:
        return i

    return -1


print(Solution().first_missing_position([3, 4, -1, 1]))
# 2