"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。


"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[pos] = nums[i]
                pos += 1
        for i in range(pos, len(nums)):
            nums[i] = 0

#双指针
class Solution(object):
     def moveZeroes(self, nums):
fast,slow=0,0 # 分别指向连续零区间的最右侧、最左侧 while fast<len(nums):
             # if nums[fast]==0 do nothing
             if nums[fast]!=0:
                 # if fast == slow shows zero isn't found yet
                 if fast > slow:# zero exists
                     nums[slow], nums[fast] = nums[fast], 0
                 slow += 1
fast += 1

