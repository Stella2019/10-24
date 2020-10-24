import heapq
import collections

class Solution(object):
  def topKFrequent(self, nums, k):
    count = collections.defaultdict(int)
    for n in nums:
      count[n] += 1

    heap = []
    for num, c in count.items():
      heap.append((-c, num))
    heapq.heapify(heap)

    result = []
    for i in range(k):
      result.append(heapq.heappop(heap)[1])
    return result

print(Solution().topKFrequent([1, 1, 1, 2, 2, 3, ], 2))
# [1, 2]