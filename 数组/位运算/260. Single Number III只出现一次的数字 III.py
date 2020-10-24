"""
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

示例 :

输入: [1,2,1,3,2,5]
输出: [3,5]
注意：

结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？

题目分析
两个不相等的元素在位级表示上必定会有一位存在不同。
将数组的所有元素异或得到的结果为不存在重复的两个元素异或的结果。
diff &= -diff 得到出 diff 最右侧不为 0 的位，也就是不存在重复的两个元素在位级表示上最右侧不同的那一位，利用这 一位就可以将两个元素区分开来。
注:-diff需要用到补码的知识，比如6的二进制是110，-6即变反加1，即001+1=010，所以-6的补码是010
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        diff = 0
        for num in nums:
            diff = diff ^ num
        diff = diff & (-diff)
        ret = [0, 0]
        for num in nums:
            if (diff & num == 0):
                ret[0] = ret[0] ^ num
            else:
                ret[1] = ret[1] ^ num
        return ret

"""思路很简单。因为数字只出现一次或两次
数字第一次出现，放进容器里。
数字再次出现，从容器里删除。
剩下来的就是两个只出现一次的数字咯。
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = set()　　　#初始化一个集合
        for i in nums:
            if i in ans:　　#数字已经存在，删除
                ans.remove(i)
            else:           #数字不存在，添加
                ans.add(i)
        return ans



"""题解
1. 用数组的方法。

定义一个数组，遍历列表。
如果数组中存在该元素就remove，否则append。
最后输出数组。
python
"""
class Solution:
    def singleNumber(self,nums:List[int])-> int:
        count=[]
        for num in nums:
            if num in count:
                count.remove(num)
            else:
                count.append(num)
        return count

"""2. 用字典的方法。

定义一个字典，遍历列表，将列表元素作为key,如果元素存在于字典中就加一，否则键值等于1。
对字典遍历，输出键值为1的key。
python
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}                  # 定义字典
        for num in nums:            # 遍历数组
            if num in count:        # 如果字典中存在当前记录
                count[num] += 1     # 次数 + 1
            else:                   # 否则
                count[num] = 1      # 当前数加入到字典中，且出现次数为1
        res=[]
        for key in count:
            if count[key]==1:
                res.append(key)
        return res
        #如果是存在一个元素可用下面的方式
        #count = {v: k for k, v in count.items()}    # 字典键值交换
        #return count[1]             # 返回出现一次的数字
""""""
3. 位运算-异或。

原理：相同元素的位运算为0；0与任意整数的异或为该整数。
分治。遍历列表，对所有元素进行异或，得到两个只出现一次的元素x,y的异或值a。
将a进行取反加一，并与a本身相与得到一个mask值，该值与列表中的每一个元素相与的结果可以作为划分数组的判别条件。
因为该mask表示了x,y二进制中不同的某一位，并且mask的其他位为0，所以列表中的元素与该值相与为0或者为1就可以将列表划分为两部分。
再对每一部分异或就可以得到最终的结果。
python
""''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=0
        x=0
        y=0
        for i in nums:
            a ^=i
        a&=~a+1
        for i in nums:
            if a&i==0:
                x ^=i
            else:
                y ^=i
        return x,y
