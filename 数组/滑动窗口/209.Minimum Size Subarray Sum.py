
"""首先创建一个sums数组来保存索引i之前所有数的和。那么当求i到j之间的和的时候，可以用来表示 sums[j] - sums[i] + nums[i]，防止重复的sum计算。(或者用一个sum变量来维护滑动窗口内所有数 的和)
滑动窗口思路:
想象一下，在一个坐标上存在两个指针left和right ，left代表滑窗的左边框，right代表滑窗的右边框。 两者通过分别向右滑动，前者能使窗口之间的和减小，后者能使窗口之间的和增大。开始时二者重合， 窗口的和就是重合点所在的数。
开始right向右滑动，使和变大。 当恰好大于等于s时，记录滑窗所包括的子数组长度ans，若ans已有数值，需判断新值是否小于旧 值，若是，更新ans。
begin向右滑动，判断是否仍大于等于s 若是，重复步骤2，3。若否，转步骤1。直到右边框到达最右边
"""
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i, j, r = 0, 0, len(nums) + 1
        sums = []
        for num in nums:
            if not sums:
                sums.append(num)
            else:
                sums.append(sums[-1] + num)
        while i < len(nums) and j < len(nums):
            if sums[j] - sums[i] + nums[i] < s:
                j += 1
            else:
                if j + 1 - i < r:
                    r=j+1-i
                i += 1
        if r != len(nums) + 1:
            return r
        else:
            return 0