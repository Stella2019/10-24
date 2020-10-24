# O(n^2) time | O(n) space
def longestIncreasingSubsequence(array):
    sequences = [None for x in array]
    lengths = [1 for x in array]  # at least 1
    maxLengthIdx = 0  # last number in LIS
    for i in range(len(array)):
        currentNum = array[i]
        for j in range(0, i):
            otherNum = array[j]
            if otherNum < currentNum and lengths[j] + 1 >= lengths[i]:
                lengths[i] = lengths[j] + 1
                sequences[i] = j
        if lengths[i] >= lengths[maxLengthIdx]:
            maxLengthIdx = i
    return buildSequence(array, sequences, maxLengthIdx)


def buildSequence(array, sequences, currentIdx):
    sequence = []
    while currentIdx is not None:
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(sequence))


# O(nlogn)time| O(n) space
def longestIncreasingSubsequence(array):
    sequences = [None for x in array]
    indices = [None for x in range(len(array) + 1)]
    length = 0
    for i, num in enumerate(array):
        newLength = binarySearch(1, length, indices, array, num)
        sequences[i] = indices[newLength - 1]
        indices[newLength] = i
        length = max(length, newLength)
    return buildSequence(array, sequences, indices[length])


def binarySearch(startIdx, endIdx, indices, array, num):
    if startIdx > endIdx:
        return startIdx
    middleIdx = (startIdx + endIdx) // 2
    if array[indices[middleIdx]] < num:
        startIdx = middleIdx + 1
    else:
        endIdx = middleIdx - 1
    return binarySearch(startIdx, endIdx, indices, array, num)


def buildSequence(array, sequences, currentIdx):
    sequence = []
    while currentIdx is not None:
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(sequence))


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        # 彩虹小本本准备好
        memo = [[1, 1] for _ in range(n)]
        max_len = 1  # 为了最后提取方便

        for j in range(n):
            tmp_max_len, count = 1, 0
            for i in range(j):
                if nums[i] < nums[j]:
                    prev_len, prev_count = memo[i][0], memo[i][1]
                    # 相当于300题里的memo[j] = max(memo[j],memo[i]+1)
                    if prev_len + 1 > tmp_max_len: tmp_max_len = prev_len + 1
                    count = 0  # reset为0，重新计数
                # 相同的长度 次数直接加一起;
                if prev_len + 1 == tmp_max_len:
                    count += prev_count
            # prev_len + 1 < tmp_max_len,跳过. 譬如232518，到18时，再见

        memo[j] = [tmp_max_len, max(count, memo[j][1])]  # count有可能是0，恢复默认
        max_len = max(tmp_max_len, max_len)

    return sum([_[1] for _ in memo if _[0] == max_len])



