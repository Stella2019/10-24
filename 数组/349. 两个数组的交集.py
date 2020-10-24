"""
给定两个数组，编写一个函数来计算它们的交集。

 

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
示例 2：

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersection(nums2, nums1)

        lookup = set()
        for i in nums1:
            lookup.add(i)

        result = []
        for i in nums2:
            if i in lookup:
                result += i,
                lookup.discard(i)
        return result

#O(M + N)|O(MIN(M,N))



class Solution:
  def intersection(self, nums1, nums2):
    results = {}
    for num in nums1:
      if num in nums2 and num not in results:
        results[num] = 1
    return list(results.keys())

  def intersection2(self, nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return [x for x in set1 if x in set2]

  def intersection3(self, nums1, nums2):
    hash = {}
    duplicates = {}
    for i in nums1:
      hash[i] = 1
    for i in nums2:
      if i in hash:
        duplicates[i] = 1

    return tuple(duplicates.keys())

print(Solution().intersection3([4, 9, 5], [9, 4, 9, 8, 4]))
# (9, 4)