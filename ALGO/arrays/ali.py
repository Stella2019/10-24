while True:
    try:
        n = int(input())
        mystr = list(map(str, input().strip().split()))
        l = list(map(int, input().strip().split()))
        if len(l) == 1:
            pass
        else:
            print()
    except EOFError:
        break
def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        # 找中位数
        if len(nums)%2 == 0:
            mid = (nums[len(nums)//2-1] + nums[len(nums)//2])//2
        else:
            mid = nums[len(nums)//2]
        ans = 0
        for num in nums:
            ans += abs(num - mid)
            # 所有数跟中位数的差的绝对值
        return ans



import sys
a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
print(smallestDifference(a, b))