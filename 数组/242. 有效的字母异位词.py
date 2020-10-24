"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

标签：哈希映射
首先判断两个字符串长度是否相等，不相等则直接返回 false
若相等，则初始化 26 个字母哈希表，遍历字符串 s 和 t
s 负责在对应位置增加，t 负责在对应位置减少
如果哈希表的值都为 0，则二者是字母异位词

"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lookup = {}

        for i in s:
            if i not in lookup:
                lookup[i] = 1
            else:
                lookup[i] += 1

        for j in t:
            if j not in lookup:
                return False
            else:
                lookup[j] -= 1

        for k in lookup:
            if lookup[k] != 0:
                return False
        return True