"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

 

示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        result = nums[0] + nums[1] + nums[len(nums) - 1]
        #sorted nums:[-4, -1, 1, 2]
        #result = (-4) + (-1) + 2
        #result > target -4 -1 1
        #result < target
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                val = nums[i] + nums[l] + nums[r]
                if abs(val - target) < abs(result - target):
                    result = val
                if val == target:
                    return target
                elif val < target:
                    l += 1
                else:
                    r -= 1
        return result