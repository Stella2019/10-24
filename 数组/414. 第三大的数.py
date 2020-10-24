"""
给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

示例 1:

输入: [3, 2, 1]

输出: 1

解释: 第三大的数是 1.
示例 2:

输入: [1, 2]

输出: 2

解释: 第三大的数不存在, 所以返回最大的数 2 .
示例 3:

输入: [2, 2, 3, 1]

输出: 1

解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
存在两个值为2的数，它们都排第二。
"""

#巧用python set和remove函数
#将数组转为set集合去除可能存在的重复元素，再判断集合的长度，若长度小于3，则返回集合的最大值，若集合长度大于等于3，
# 即原数组存在第三大的元素，则连续两次删除集合最大元素，得到的集合的最大值即为原数组的第三大元素。时间复杂度为O(n)
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        set_nums = set(nums)
        if len(set_nums) < 3:
            return max(set_nums)
        else:
            set_nums.remove(max(set_nums))
            set_nums.remove(max(set_nums))
            return max(set_nums)

#三个指针x1,x2,x3对数组进行遍历,始终保持x1 > x2 > x3,最后返回x3即可
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        x1,x2,x3 = nums[0],nums[0],nums[0]
        # 找到x2初始值
        for i in range(1,len(nums)):
            if nums[i] != x1 and x1 == x2:
                if nums[i] > x1:
                   x1,x2 = nums[i],x1
                else:
                    x2 = nums[i]
                break
        for j in range(i + 1,len(nums)):
                # 找到x3初始值
                if x3 == nums[0]:
                    if nums[j] != x1 != x2:
                        if nums[j] > x1:
                          x1,x2,x3 = nums[j],x1,x2
                        elif x1 > nums[j] > x2:
                            x2,x3 = nums[j],x2
                        else:
                            x3 = nums[j]
                    continue
                # 保持x1,x2,x3的大小顺序
                if nums[j] > x1:
                   x1,x2,x3 = nums[j],x1,x2
                elif  x1 > nums[j] > x2:
                   x2,x3 = nums[j],x2
                elif x3 < nums[j] < x2:
                   x3 = nums[j]
        return x3 if x1 != x2 != x3 else x1





class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))

        if len(nums) < 3:
            return max(nums)
        else:
            nums[-3]


class Solution(object):
    def thirdMax(self, array):
        """
        :type nums: List[int]
        :rtype: int
        """
        position = 3 - 1
        return quickselectHelper(array, 0, len(array) - 1, position)

    def quickselectHelper(array, startIdx, endIdx, position):
        while True:
            if startIdx > endIdx:
                raise Exception("Your algorithm should never arrive here!")
            pivotIdx = startIdx
            leftIdx = startIdx + 1
            rightIdx = endIdx
            while leftIdx <= rightIdx:
                if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
                    swap(leftIdx, rightIdx, array)
                if array[leftIdx] <= array[pivotIdx]:
                    leftIdx += 1
                if array[rightIdx] >= array[pivotIdx]:
                    rightIdx -= 1
            swap(pivotIdx, rightIdx, array)
            if rightIdx == position:
                return array[rightIdx]
            elif rightIdx < position:
                startIdx = rightIdx + 1
            else:
                endIdx = rightIdx - 1

    def swap(one, two, array):
        array[one], array[two] = array[two], array[one]



