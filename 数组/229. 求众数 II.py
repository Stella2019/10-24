"""
给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。

示例 1:

输入: [3,2,3]
输出: [3]
示例 2:

输入: [1,1,1,3,3,2,2,2]
输出: [1,2]

设c为众数以外的数的总和，a, b为超过1/3的众数的频数，有三种情况：
(1)a,b均超过1/3;
(2)a,b中有一个超过;
(3)a,b中没有一个超过
因此可以采用摩尔投票法

"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a, b, count_a, count_b = 0, 0, 0, 0 # 设定1号众数和2号众数
        res = []

        for i in nums:
            if a == i: # 频数统计的优先顺序要大于频数为0的判断
                count_a += 1
                continue
            if b == i:
                count_b += 1
                continue
            if count_a == 0:
                a = i
                count_a = 1
                continue
            if count_b == 0:
                b = i
                count_b = 1
                continue
            count_a -= 1
            count_b -= 1

        count_a, count_b = 0, 0 # 重置计数器
        for j in nums: # 再检验
            if j == a:
                count_a += 1
            elif j == b:
                count_b += 1
        if count_a > len(nums)/3:
            res.append(a)
        if count_b > len(nums)/3:
            res.append(b)
        return res

#python使用Counter, 7行代码搞定
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        cnt = collections.Counter(nums)
        count = len(nums) / 3

        for k, v in cnt.items():
            if v > count:
                ans.append(k)

        return ans


"""
摩尔投票法。适用于找出所有出现超过n/k次的元素。以k=3为例。该情况下，最多2个候选cand1和cand2。

第一轮对抗，cand1和cand2的初始计数分别为0。遍历数组，如果当前值和cand1或者cand2相等，则计数+1，如果有候选空缺，补上。否则说明当前数与任何一个候选不相等，给每个候选的计数-1。
第二轮统计，计算后得出cand1和cand2，如果对应的cnt1和cnt2不为0，则在循环遍历一次数组，统计cand1和cand2的出现次数，如果大于n/3即可。
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1 = cand2 = None
        cnt1 = cnt2 = 0
        for num in nums:
            if num == cand1:
                cnt1 += 1
                continue
            if num == cand2:
                cnt2 += 1
                continue
            if cnt1 == 0:
                cand1 = num
                cnt1 += 1
                continue
            if cnt2 == 0:
                cand2 = num
                cnt2 += 1
                continue
            cnt1 -= 1
            cnt2 -= 1
        ret = []
        if cnt1 > 0:
            cnt1 = 0
            for num in nums:
                if num == cand1:
                    cnt1 += 1
            if cnt1 > len(nums) // 3:
                ret.append(cand1)
        if cnt2 > 0:
            cnt2 = 0
            for num in nums:
                if num == cand2:
                    cnt2 += 1
            if cnt2 > len(nums) // 3:
                ret.append(cand2)
        return ret




 
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1, num2 = 0, 0
        c1, c2 = 0, 0
        result = []

        for i in nums:
            if i == num1:
                c1 += 1
            elif i == num2:
                c2 += 1
            elif c1 == 0:
                num1 = i
                c1 = 1
            elif c2 == 0:
                nums2 = i
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
            #往下减一 num1 = 1, c1 = 3, num2 = 3, c2 = 2  ->c2= 0
            #nums2 = i, num = 2, c2 = 1

        c1 = 0
        c2 = 0  #清0
        for j in nums:
            if j == num1:
                c1 += 1
            elif j == num2:
                c2 += 1
        l = len(nums)
        if c1 > l//3:
            result.append(num1)
        if c2 > l//3:
            result.append(num2)
        return result