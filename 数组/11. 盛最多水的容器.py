"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。
示例：

输入：[1,8,6,2,5,4,8,3,7]
输出：49
求的是面积
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        result = 0

        while left < right:
            water = min(height[left], height[right]) * (right - left)
            if water > result:
                result = water
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result







class Solution:
    def trap(self, height: List[int]) -> int:
        lmax, rmax, res = 0, 0, 0
        for i in range(len(height)):
            lmax = max(lmax, height[i])
            rmax = max(rmax, height[-1-i])
            res += lmax + rmax - height[i]
        return res - lmax * len(height)


# 方法2：从最高点分成两块，求总面积，然后减去柱子面积，时间复杂度O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        m,minx = 0, 0
        sumh = 0
        for idx,num in enumerate(height):
            sumh += height[idx]
            if num >= m:
                m = num
                minx = idx
        cnt = 0
        maxi, maxj = 0, 0
        for i in range(minx):
            maxi = max(maxi,height[i])
            cnt += maxi
        for j in reversed(range(minx,len(height))):
            maxj = max(maxj,height[j])
            cnt += maxj
        return sumh

if __name__=='__main__':
    height = list(map(int, input().split('')))
    print(trap(height))



select avg(med) as med
from
(
    select t1.number,t1.sale
    from orders t1 left join orders t2
    on t1.shop_id = t2.shop_id
    group by t1.shop_id,t1.shop_id
    having sum(case
	    when t1.sale = t2.sale then 1
	    else 0
    end) >= abs(sum(sign(t1.sale - t2.sale)))
)t
group by t.shop_id
