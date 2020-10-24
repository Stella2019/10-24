"""
给你一个 严格升序排列 的正整数数组 arr 和一个整数 k 。

请你找到这个数组里第 k 个缺失的正整数。

示例 1：

输入：arr = [2,3,4,7,11], k = 5
输出：9
解释：缺失的正整数包括 [1,5,6,8,9,10,12,13,...] 。第 5 个缺失的正整数为 9 。
示例 2：

输入：arr = [1,2,3,4], k = 2
输出：6
解释：缺失的正整数包括 [5,6,7,...] 。第 2 个缺失的正整数为 6 。
"""
"""解法2：利用arr[i]与其下标i关系
不难发现，一个不缺失元素的序列，会有arr[i]=i+1这样的关系，而在缺失元素之后，
会有arr[i]>i+1，简单移项可得 arr[i]-i-1 > 0，缺失一个的时候，相差1，两个则相差2，
以此类推，缺失越多，两者差距越大，我们要找第k个缺失的，换言之，只要arr[i]-i-1 == k,
我们便找到了题目要找的数字。
"""

    def findKthPositive(self, arr: List[int], k: int) -> int:
        #step 1: num = 1
        #   compare arr[0] ?= num
        #                     == num += 1
        #                     != current num => missing calue => result = num = 1
        #                      k -= 1 arr[0] -> arr[0]
        #step 2: num = 2
        #   compare arr[0] ? = num
        #                    == num += 1
        #                     != current num => missing calue => result = num = 1
        #                     k = 4
        #step 3: num = 3
        #   compare arr[1] ? = num
        #                    == num += 1
        #                     != current num => missing calue => result = num = 1
        #                     k = 4
        #step 4: num = 4
        #      compare arr[2] ?= num
        #                      != current num=> missing calue=>tmp result = current num = 1    k = 4
        #step5: num = 5
        #       compare arr[3] ?= num
        #                      == num+1 arr[2] -> arr[3] new missing calue=>tmp result = current num = 5
        #step 6: num = 6
        #compare arr[3]?= num
        #!= current num => new missing value => temp result = current num = 6
        # k -= 1 = 2      arr[3] -> arr[3]

        #关键arr, num,k(k每次找到一个就-1)k = 0的时候
        num = 1
        n = len(arr)
        for i in range(0, n):
            while arr[i] != num and k != 0:
                #arr = [11,12,14] k = 2
                #missing
                result = num
                num += 1
                k -= 1
            if k == 0:
                return result
            else:
                num += 1
        result = num - 1
        while k>0:
            result += 1
            k -= 1
        return result
        #time o(n+k)
        #space o(1)

#follow up:二分法寻找
"""
解法3：二分查找
然而上述的解法没有用上题目给出的条件 严格升序排列，已经找出了 arr[i]-i-1 > 0关系之后，我们可以利用上述的线性查找的方式改为二分查找的方式。
"""
class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        #arr = [2,3,4,7,11], k = 5
        #positive number = 1,2,3,4,5..
        #missing number = arr[index] - (index+1)
        #missing number = arr[4]-(4+1) = 11-5=6
        #     k = 5? result在中间
        #missing number = arr[3]-(3+1) = 7-4 = 3
        #missing number = arr[2] -(2+1) = 4-3 = 1
        #index = existing value#
        #k = missing#
        #result = low_index + k
        low, high = 0, len(arr)
        while low < high:
            mid = (low + high)//2
            if arr[mid] - (mid + 1) < k:
                low = mid + 1
            else:
                high = mid
        return low + k
    #IMEO(LOGN)
    #SPACEO(1)
