"""
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2

排序，最中间次数多于N/2
根据数组的特点，出现次数超过一半的数，他出现的次数比其他数字出现的总和还要多，因此可以最开始保存两个数值：
数组中的一个数字以及它出现的次数，然后遍历，如果下一个数字等于这个数字，那么次数加一，如果不等，次数减一，当次数
等于0的时候，在下一个数字的时候重新复制新的数字以及出现的次数置为1，直到进行到最后，然后再验证最后留下的数字是否
出现次数超过一半，因为可能前面的次数依次抵消掉，最后一个数字就直接是保留下来的数字，但是出现次数不一定超过一半。

本题还可以利用 Boyer- Moore Majority Vote Algorithm 来解决这个问题，使得时间复杂度为 O (N）。
可以这么理解该算法：使用 cnt 来统计一个元素出现的次数，当遍历到的元素和统计元素不相等时，
令 cnt-=1。如果前面查找了 i 个元素，且 cnt==0, 说明前 i 个元素没有 majority，或者有 majority，
但是出现的次数少于 i2, 因为如果多于 i2 的话 cnt 就一定不会为 0。
此时剩下的 n-i个元素中  majority I的数目依然多于（n-i)/2,因此继续查找就能持找出 majority

"""


def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = sorted(nums)
    return nums[len(nums) // 2]

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        majority = nums[0]
        for num in nums:
            if cnt == 0:
                majority == nums
            if majority == num:
                cnt += 1
            else:
                cnt -= 1
        return majority


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        # 这个操作就是建立在出现次数超过一半的数，他出现的次数比其他数字出现的总和还要多，所以如果存在这个数，最后count
        # 肯定不为0的
        count = 1
        number = numbers[0]
        for i in numbers[1:]:
            if number == i:
                count += 1
            else:
                count -= 1
                if count == 0:
                    number = i
                    count += 1

        sum = 0
        for j in numbers:
            if j == number:
                sum += 1

        return number if sum > len(numbers) // 2 else 0