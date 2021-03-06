"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

题目分析
2有两种，3有三种，4有五种，5有八种，6有13种，其实这是一个斐波那契数，不过今天我们要用动态规划的思想来 求解这个问题。
递归和动态规划都是将原问题拆成多个子问题然后求解，他们之间最本质的区别是，动态规划保存了子问题的解，避
免重复计算。
定义一个数组 dp 存储上楼梯的方法数(为了方便讨论，数组下标从 1 开始)，dp[i] 表示走到第 i 个楼梯的方法数 目。
第 i 个楼梯可以从第 i-1 和 i-2 个楼梯再走一步到达，走到第 i 个楼梯的方法数为走到第 i-1 和第 i-2 个楼梯的方法数 之和。
考虑到 dp[i] 只与 dp[i - 1] 和 dp[i - 2] 有关，因此可以只用两个变量来存储 dp[i - 1] 和 dp[i - 2]，使得原来的 O(N) 空 间复杂度优化为 O(1) 复杂度。

"""
 class Solution:
     def climbStairs(self, n: int) -> int:
         if n < 3:
             return n
# pre1是i-1，pre2是i-2
         pre2, pre1 = 1, 2
         for i in range(2, n):
             pre1, pre2 = pre1 + pre2, pre1
         return pre1








def staircase(n):
  if n <= 1:
    return 1
  return staircase(n-1) + staircase(n-2)


def staircase2(n):
  prev = 1
  prevprev = 1
  curr = 0

  for i in range(2, n + 1):
    curr = prev + prevprev

    prevprev = prev
    prev = curr
  return curr


print(staircase(5))
# 8

print(staircase2(5))
# 8