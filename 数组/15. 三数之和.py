"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
排序 + 双指针
本题的难点在于如何去除重复解。

算法流程：
特判，对于数组长度 nn，如果数组为 nullnull 或者数组长度小于 33，返回 [][]。
对数组进行排序。
遍历排序后数组：
若 nums[i]>0nums[i]>0：因为已经排序好，所以后面不可能有三个数加和等于 00，直接返回结果。
对于重复元素：跳过，避免出现重复解
令左指针 L=i+1L=i+1，右指针 R=n-1R=n−1，当 L<RL<R 时，执行循环：
当 nums[i]+nums[L]+nums[R]==0nums[i]+nums[L]+nums[R]==0，执行循环，判断左界和右界是否和下一位置重复，去除重复解。并同时将 L,RL,R 移到下一位置，寻找新的解
若和大于 00，说明 nums[R]nums[R] 太大，RR 左移
若和小于 00，说明 nums[L]nums[L] 太小，LL 右移
复杂度分析
时间复杂度：O\left(n^{2}\right)O(n
2
 )，数组排序 O(N \log N)O(NlogN)，遍历数组 O\left(n\right)O(n)，双指针遍历 O\left(n\right)O(n)，总体 O(N \log N)+O\left(n\right)*O\left(n\right)O(NlogN)+O(n)∗O(n)，O\left(n^{2}\right)O(n
2
 )
空间复杂度：O(1)O(1)

"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #nums.sort()
        #[-4,-1,0,1,2]
        #result = []
        #while/for
        #[0,1, 2, 3, 4....]
        #0+1+2=3>0

        #[-100,0,1,2,3,...9]
        n= len(nums)
        result = []
        nums.sort()
        for i in range(n-2):
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            if nums[i] + nums[n-2] + nums[n-1] < 0:
                continue
            if 0 < i and nums[i] == nums[i - 1]:
                continue

            l, r = i+1, n-1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    while l+1 < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
                    while l< r-1 and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1
                elif tmp < 0:
                    l += 1
                else:
                    r -= 1
        return result









class Solution:
  def threeSumBruteForce(self, nums):
    result = []
    for i1 in range(0, len(nums)):
      for i2 in range(i1+1, len(nums)):
        for i3 in range(i2+1, len(nums)):
          a, b, c = nums[i1], nums[i2], nums[i3]
          if a + b + c == 0:
            result.append([a, b, c])
    return result

  def threeSumHashmap(self, nums):
    nums.sort()
    result = []
    for i in range(len(nums)):
      self.twoSumHashmap(nums, i, result)
    return result

  def twoSumHashmap(self, nums, start, result):
    values = {}
    target = -nums[start]
    for i in range(start+1, len(nums)):
      n = nums[i]
      diff = target - n
      if diff in values:
        result.append([n, diff, nums[start]])
      values[n] = 1

  def threeSumIndices(self, nums):
    nums.sort()
    result = []
    for i in range(len(nums)):
      self.twoSumIndices(nums, i, result)
    return result

  def twoSumIndices(self, nums, start, result):
    low = start + 1
    high = len(nums) - 1
    while low < high:
      sum = nums[start] + nums[low] + nums[high]
      if sum == 0:
        result.append([nums[start], nums[low], nums[high]])
        low += 1
        high -= 1
      elif sum < 0:
        low += 1
      else:
        high -= 1


print(Solution().threeSumBruteForce([-1, 0, 1, 2, -4, -3]))
# [[-1, 0, 1], [1, 2, -3]]

print(Solution().threeSumHashmap([-1, 0, 1, 2, -4, -3]))
# [[2, 1, -3], [1, 0, -1]]

print(Solution().threeSumIndices([-1, 0, 1, 2, -4, -3]))
# [[-3, 1, 2], [-1, 0, 1]]
