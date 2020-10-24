"""class Solution:
    def twoSum(self, array: List[int], targetSum: int) -> List[int]:
        left = 0
        right = len(array) - 1
        while left < right:
            currentSum = array[left] + array[right]
            if currentSum == targetSum:
                return [array[left], array[right]]
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
        return [left + 1, right + 1]
"""
class Solution(object):
    def twoSum(self, numbers, target):
        start = 0
        end = len(numbers) - 1

        while start != end:
            sum = numbers[start] + numbers[end]
            if sum > target:
                end -= 1
            elif sum < target:
                start += 1
            else:
                return [start + 1, end + 1]