给定两个有序数组arr1和arr2，已知两个数组的长度都为N，求两个数组中所有数的上中位数。
上中位数：假设递增序列长度为n，若n为奇数，则上中位数为第n/2+1个数；否则为第n个数
[要求]
时间复杂度为O(logN)O(logN)，额外空间复杂度为O(1)O(1)


#
# find median in two sorted array
# @param arr1 int整型一维数组 the array1
# @param arr2 int整型一维数组 the array2
# @return int整型
#
class Solution:
    def findMedianinTwoSortedAray(self, arr1, arr2):
        if not arr1 or not arr2:
            return -1
        n = len(arr1)
        l1, r1, l2, r2 = 0, n - 1, 0, n - 1
        while l1 < r1:
            m1 = (l1 + r1) // 2
            m2 = (l2 + r2) // 2
            length = r1 - l1 + 1
            if arr1[m1] < arr2[m2]:
                l1 = m1 + (1 if length % 2 == 0 else 0)
                r2 = m2
            elif arr1[m1] > arr2[m2]:
                l2 = m2 + (1 if length % 2 == 0 else 0)
                r1 = m1
            else:
                return arr1[m1]
        return min(arr1[l1], arr2[l2])



对python真的不友好
# min edit cost
# @param str1 string字符串 the string
# @param str2 string字符串 the string
# @param ic int整型 insert cost
# @param dc int整型 delete cost
# @param rc int整型 replace cost
# @return int整型
#
class Solution:
    def minEditCost(self , str1 , str2 , ic , dc , rc ):
        # write code here
        n=len(str1)
        m=len(str2)
        dp=[[ 0 for _ in range(n+1)] for _ in range(m+1)]
        for j in range(1,n+1):
            dp[0][j]=dp[0][j-1]+min(ic,dc,rc)
        for i in range(1,m+1):
            dp[i][0]=dp[i-1][0]+min(ic,dc,rc)
        for i in range(1,m+1):
            for j in range(1,n+1):
                if str2[i-1]==str1[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i][j-1]+ic,dp[i-1][j]+dc,dp[i-1][j-1]+rc)
        return  dp[-1][-1]







"""
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]


思路1：全部考虑，选或不选
看起来我们并不需要遍历，而是需要每一层都考虑一下当前元素的index对应的值，我们是要还是不要，依然是传入一个index元素用于指向当前层的元素索引【回溯三要素之2.回溯范围】
能够看出来灰色部分就是重复答案，红色框起来的部分就是重复答案的条件，也就是我们要提前就剪枝的部分，依然类似于47.全排列II，发现当遇到重复元素，且上一个元素未被使用过，就需要剪枝【回溯三要素之3.剪枝条件】，依然可以用一个check变量来保存元素是否有被使用过

思路1：回溯三要素
结合78.子集和47.全排列II就很好想到回溯三要素是什么了：

有效结果
当指向元素的index==len(nums)的时候，就说明这一次的搜索结束了
if index == len(nums):
    self.res.append(sol)
    return

回溯范围及答案更新
不需要循环遍历，而只需要用一个index指向每一次的元素，下一层更新index = index+1
对于答案更新，我们需要考虑选或不选当前答案，保存当前index指向的元素

self.backtrack(sol+[nums[index]], index+1, nums)
self.backtrack(sol, index+1, nums)

剪枝条件
当当前元素和前一个元素值相同（此处隐含这个元素的index>0），并且前一个元素还没有被使用过的时候，我们要剪枝
但是有一个注意的地方：
对于选或不选：只有选的时候才需要判断是否剪枝，如果根本不选，那么就不需要剪枝了


思路2：顺序考虑，仅考虑选择的元素
以空集[]开始，从第一个元素开始考虑，它有三种选择，1,1',2，组成[1]，[1']，[2]
此时我们就发现，有了重复的答案，于是我们就应该剪枝：1'前面的1是相同的元素，此时发现上一个在此时是没有用过，那么就满足了我们的剪枝条件，保留[1],[2]
当第一个元素为1的时候，第二个元素可以选择的是1后面的元素1',2，组成[1,1']，[1,2]
当第二个元素为1'的时候，第二个元素可以选择2，组成[1,1',2]
结束遍历，获得组成的8个答案，这说明了有效结果是没有条件的，任何结果都是有效的，因为无效的已经被剪枝掉了

回溯三要素
有效结果
没有条件，所有结果都是有效结果
self.res.append(sol)
回溯范围及答案更新
需要循环遍历，并且是部分遍历，只考虑当前元素之后的元素们，所以需要传入一个index表示起点
！！！index仅用于表示起点，回溯的递归还是遍历的每个元素
对于答案更新，依然是累加当前元素

for i in range(index, len(nums)):
    if i > 0 and nums[i] == nums[i-1] and check[i-1] == 0:
        continue
    check[i] = 1
    self.backtrack(sol+[nums[i]], i+1, nums, check)
    check[i] = 0
剪枝条件
当当前元素和前一个元素值相同（此处隐含这个元素的index>0），并且前一个元素还没有被使用过的时候，我们要剪枝
但是有一个注意的地方：

if i > 0 and nums[i] == nums[i-1] and check[i-1] == 0:
    continue
"""


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []
        check = [0 for i in range(len(nums))]

        self.backtrack([], 0, nums, check)

        return self.res

    def backtrack(self, sol, index, nums, check):
        if index == len(nums):
            self.res.append(sol)
            return

        if not (index > 0 and nums[index] == nums[index - 1] and check[index - 1] == 0):
            check[index] = 1
            self.backtrack(sol + [nums[index]], index + 1, nums, check)
            check[index] = 0
        '''如果不选这个元素，不需要判断是否剪枝'''
        self.backtrack(sol, index + 1, nums, check)


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        check = [0 for i in range(len(nums))]

        self.backtrack([], 0, nums, check)

        return self.res

    def backtrack(self, sol, index, nums, check):
        self.res.append(sol)

        for i in range(index, len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 0:
                continue
            check[i] = 1
            self.backtrack(sol + [nums[i]], i + 1, nums, check)
            check[i] = 0


Trick：空间优化
其实在这道题还有一个小的trick可以再在上面代码的基础上做空间优化【减少额外空间的使用（但为毛提交效果不咋好。。。。）】
但这里和46.全排列和47.全排列II不同的是，求子集不需要考虑用过的元素不能再用了，这里只需要考虑上一个相同元素是否有被使用，那么我们完全可以不用传入check数组去保存状态，我们只需要在函数的入参加一个boolean变量【0 - 1
来表示】来保存上一个元素的使用情况：

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []

        self.backtrack([], 0, nums, 0)

        return self.res

    def backtrack(self, sol, index, nums, pre_used):
        if index == len(nums):
            self.res.append(sol)
            return

        if not (index > 0 and nums[index] == nums[index - 1] and pre_used == 0):
            pre_used = 1
            self.backtrack(sol + [nums[index]], index + 1, nums, pre_used)
            pre_used = 0
        self.backtrack(sol, index + 1, nums, 0)


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []

        self.backtrack([], 0, nums, 0)

        return self.res

    def backtrack(self, sol, index, nums, pre_used):
        self.res.append(sol)

        for i in range(index, len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and pre_used == 0:
                continue
            pre_used = 1
            self.backtrack(sol + [nums[i]], i + 1, nums, pre_used)
            pre_used = 0



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








"""
给出一个完全二叉树，求出该树的节点个数。

说明：

完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。

示例:

输入:
    1
   / \
  2   3
 / \  /
4  5 6

输出: 6

"""
"""
方法一：线性时间
算法：O(N)O(LOGN)

最简单的解决方法就是用递归一个一个的计算节点。
"""


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return 1 + self.countNodes(root.right) + self.countNodes(root.left) if root else 0


"""方法二：二分搜索
方法一没有利用完全二叉树的特性。完全二叉树中，除了最后一层外，其余每层节点都是满的，并且最后一层的节点全部靠向左边。

这说明如果第 k 层不是最后一层，则在第 k 层中将有 2^k 个节点。由于最后一层可能没有完全填充，则节点数在 1 到 2^d 之间，其中 d 指的是树的高度。
我们可以直接计算除了最后一层以外的所有结点个数：\sum_{k = 0}^{k = d - 1}{2^k} = 2^d - 1∑
 那么我们可以将问题简化为计算完全二叉树最后一层有多少个节点。

现在有两个问题：

最后一层我们需要检查多少个节点？
一次检查的最佳的时间性能是什么？
让我们从第一个问题开始思考。最后一层的叶子节点全部靠向左边，我们可以用二分搜索只检查 \log(2^d) = dlog(2
d
 )=d 个叶子代替检查全部叶子。


让我们思考第二个问题，最后一层的叶子节点索引在 0 到 $2^d - 1$ 之间。如何检查第 idx 节点是否存在？
让我们来用二分搜索来构造从根节点到 idx 的移动序列。如，idx = 4。idx 位于 0,1,2,3,4,5,6,7 的后半部分，
因此第一步是向右移动；然后 idx 位于 4,5,6,7 的前半部分，因此第二部是向左移动；idx 位于 4,5 的前半部分，
因此下一步是向左移动。一次检查的时间复杂度为 \mathcal{O}(d2) )。

如果树为空，返回 0。
计算树的高度 d。
如果 d == 0，返回 1。
除最后一层以外的所有节点数为 2^d-1。最后一层的节点数通过二分搜索，检查最后一层有多少个节点。使用函数 exists(idx, d, root) 检查第 idx 节点是否存在。
使用二分搜索实现 exists(idx, d, root)。
返回 2^d - 1 + 最后一层的节点数。

"""


class Solution:
    def compute_depth(self, node: TreeNode) -> int:
        """
        Return tree depth in O(d) time.
        """
        d = 0
        while node.left:
            node = node.left
            d += 1
        return d

    def exists(self, idx: int, d: int, node: TreeNode) -> bool:
        """
        Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        Return True if last level node idx exists.
        Binary search with O(d) complexity.
        """
        left, right = 0, 2 ** d - 1
        for _ in range(d):
            pivot = left + (right - left) // 2
            if idx <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1
        return node is not None

    def countNodes(self, root: TreeNode) -> int:
        # if the tree is empty
        if not root:
            return 0

        d = self.compute_depth(root)
        # if the tree contains 1 node
        if d == 0:
            return 1

        # Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        # Perform binary search to check how many nodes exist.
        left, right = 1, 2 ** d - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if self.exists(pivot, d, root):
                left = pivot + 1
            else:
                right = pivot - 1

        # The tree contains 2**d - 1 nodes on the first (d - 1) levels
        # and left nodes on the last level.
        return (2 ** d - 1) + left
