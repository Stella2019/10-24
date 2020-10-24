class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        # r先申请好n个位置，防止append时发生扩容耗费时间
        r, s = [0] * len(nums), 0

        for i, num in enumerate(nums):
            s += num
            r[i] = s
        return r