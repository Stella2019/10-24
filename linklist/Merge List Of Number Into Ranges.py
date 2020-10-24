def makerange(low, high):
  return str(low) + '-' + str(high)


def findRanges(nums):
  if not nums:
    return []

  ranges = []
  low = nums[0]
  high = nums[0]

  for n in nums:
    if high + 1 < n:
      ranges.append(makerange(low, high))
      low = n
    high = n
  ranges.append(makerange(low, high))
  return ranges


print(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
# ['0-2', '5-5', '7-11', '15-15']