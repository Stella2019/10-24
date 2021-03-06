class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], 0, nums)
        return self.res

    def backtrack(self, sol, index, nums):
        if index == len(nums):
            self.res.append(sol)
            return

        self.backtrack(sol + [nums[index]], index + 1, nums)
        self.backtrack(sol, index + 1, nums)


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], 0, nums)

        return self.res

    def backtrack(self, sol, index, nums):
        self.res.append(sol)

        for i in range(index, len(nums)):
            self.backtrack(sol + [nums[i]], i + 1, nums)

