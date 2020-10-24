"""
给定一个包含 n 个整数的数组，找到最大平均值的连续子序列，且长度大于等于 k。并输出这个最大平均值。

样例 1:

输入: [1,12,-5,-6,50,3], k = 4
输出: 12.75
解释:
当长度为 5 的时候，最大平均值是 10.8，
当长度为 6 的时候，最大平均值是 9.16667。
所以返回值是 12.75。
 

注释 :

1 <= k <= n <= 10,000。
数组中的元素范围是 [-10,000, 10,000]。
答案的计算误差小于 10-5 。
"""
#滑动窗口
"""
看到答案的计算误差小于 \ 10^{-5} 10 
−5
 ，果断二分。

题目要求所有长度大于等于 kk 的区间平均值的最大值。很容易想到直接暴力求所有平均值，时间复杂度是 O(n^2)O(n 
2
 )，当然不行。而由于平均值和前缀和 (pre\_sum)(pre_sum)、区间长度两个变量有关，不具有单调性，必须去掉一个变量的影响。

avg(start,\ end)=\frac{sum(nums[start:end+1])}{end-start}
avg(start, end)= 
end−start
sum(nums[start:end+1])
​	
 

要去掉区间长度的影响，需要归一化，将区间内每个数减去平均值，使 avg(start,\ end)=0avg(start, end)=0：

sum(nums[start:end+1])\ =\ avg(start,\ end)\ *\ (end-start)\\ => sum(num-avg(start,\ end))\ =\ 0*(end-start)\ =\ 0,\ num\ in\ nums[start:end+1]
sum(nums[start:end+1]) = avg(start, end) ∗ (end−start)
=>sum(num−avg(start, end)) = 0∗(end−start) = 0, num in nums[start:end+1]

可是对每个区间，avg(start,\ end)avg(start, end) 都不一样。

既然直接求求不了，那就猜。就像 Leetcode.374 猜数字大小 一样 ，我们先猜一个 avgavg，看它大了还是小了，进而二分查找得到答案。

猜小了：

avg\ \le\ max(avg(所有区间)) \\ =>\ avg-avg\ \le\ max(avg(某区间)-avg) \\ =>\ max(\frac{sum(nums[某区间，每个数都减avg])}{区间长})\ \ge\ 0
avg ≤ max(avg(所有区间))
=> avg−avg ≤ max(avg(某区间)−avg)
=> max( 
区间长
sum(nums[某区间，每个数都减avg])
​	
 ) ≥ 0

也就是求长度大于等于 kk 的区间和最大值是否大于等于零。这个问题可以是 643.最大平均子数组和 的进阶版，需要多维护一个变量。具体见代码。

解决了 checkcheck 函数，现在就可以二分了。
 
"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        def check(avg):
            # 如果是求长度等于 k 的区间的区间和：
            # 使用滑动窗口，维护首尾前缀和（见643.最大平均子段和）
            # 这一题是大于等于 k
            # 我们需要知道以 end 结尾，长度大于等于 k 的区间中最大的区间和
            # 多维护一个 start_sum 的最小值即可
            # end_sum - min_sum 即为所求区间和最大值
            end_sum = sum(num - avg for num in nums[:k])
            start_sum = min_start_sum = 0
            for end in range(k, len(nums)):
                if end_sum >= min_start_sum:
                    return True
                end_sum += nums[end] - avg
                start_sum += nums[end-k] - avg
                min_start_sum = min(min_start_sum, start_sum)
            return end_sum >= min_start_sum
        # 二分法
        l, r = min(nums), max(nums)
        while r - l > 1e-5:
            mid = (l+r) / 2
            if check(mid):  # 存在符合条件的区间，其平均值大于等于 mid，下界向上收缩
                l = mid
            else:
                r = mid
        return l
 


