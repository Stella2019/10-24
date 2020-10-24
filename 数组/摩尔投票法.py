"""
解题思路
摩尔投票法，是用来在线性时间内，寻找出现次数最多的n个元素的算法。
基本思路，如果只寻找最大的一个元素，比如169题。
具体思路见注释：
记住一点你就可以理解摩尔投票法：candi永远表示最大相对票数的候选元素，candi_count对应其相对票数
"""
#229
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        用摩尔投票法
        首先一点，要选择出现次数大于n/3的数字，最多只能有两个。
        所以问题转化为：1.寻找得票最高的两个数() 2.判断得票数是否大于n/3。
        第一步，使用”摩尔投票法“来选择得票最高的前n个数

        """
        # 计算得票最多的两个候选数字，初始化
        candi1, candi2, c1_count, c2_count = 0, 0, 0, 0
        for num in nums:
            # 更新candi1的**相对**票数
            if num == candi1:
                c1_count += 1
                continue
            # 更新candi2的**相对*票数
            if num == candi2:
                c2_count += 1
                continue
            # 如果不是candi1和candi2，更换candi1，并更新**相对*票数
            if c1_count == 0:
                candi1 = num
                c1_count = 1
                continue
            # 同理更换candi1，并更新**相对*票数
            if c2_count == 0:
                candi2 = num
                c2_count = 1
                continue
            # 如果都不满足上面条件，说明出现了新的元素。但是因为**相对*票数都大于0的，所以此时最大票数的两个数还是candi1和candi2，所以需要同时将**相对*票数减一
            c1_count -= 1
            c2_count -= 1

        # print("candi1:%s, candi2:%s" % (candi1, candi2))

        # 遍历计算两个候选人各自的的**真实**票数
        c1_count, c2_count = 0, 0
        for num in nums:
            if num == candi1:
                c1_count += 1
                continue
            if num == candi2:
                c2_count += 1
                continue
        # 选出**真实**得票数大于len(nums) // 3的候选人
        result = []
        if c1_count > len(nums) // 3:
            result.append(candi1)
        if c2_count > len(nums) // 3:
            result.append(candi2)
        return result

#169题：

def majorityElement(nums: List[int]):
    # 摩尔投票法
    # candi永远表示最大相对票数的候选元素，candi_count对应其相对票数
    candi, candi_count = nums[0], 1
    for num in nums:
        # 表示直到当前num，并没有候选元素，就是没有一个元素的票数>0的
        if candi_count == 0:
            candi = num
            candi_count = 1
            continue
        # 当前num等于候选元素，则候选元素增加一票
        if candi == num:
            candi_count += 1
        else:
            candi_count -= 1  # 当前num不等于候选元素，并且最大票数大于0，只需要把最大票数减一，候选元素不变

    return candi

