class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, j in enumerate(nums):
            if target - j in dic:
                return [dic[target - j], i]
            else:
                dic[j] = i


class Solution:
    def twoSum(selfself, nums, target):
        for i in nums:
            j = target - i
            start_index = nums.index(i)
            next_index = start_index + 1
            temp_nums = nums[next_index: ]
            if j in temp_nums:
                return (nums.index(i), next_index + temp_nums.index(j))





class Solution(object):
  def twoSum(self, nums, target):
    for i1, a in enumerate(nums):
      for i2, b in enumerate(nums):
        if a == b:
          continue
        if a + b == target:
          return [i1, i2]
    return []

  def twoSumB(self, nums, target):
    values = {}
    for i, num in enumerate(nums):
      diff = target - num
      if diff in values:
        return [i, values[diff]]
      values[num] = i
    return []


print(Solution().twoSumB([2, 7, 11, 15], 18))
