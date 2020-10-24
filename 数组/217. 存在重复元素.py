"""
给定一个整数数组，判断是否存在重复元素。

如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

 

示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #1.go over each element in the array
        #find if any value matches
        # creat a dictionary
        # if new element in dictionary, return true
        #if not, return false

        #2.sort array, i.e. after sorted[1, 1, 2, 3]
        # if nums[i] = ? nums[i + 1], return true if  ==
        # return false if !=
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False