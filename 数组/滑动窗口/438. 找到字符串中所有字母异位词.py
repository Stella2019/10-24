"""给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始 索引。
字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。 说明:
  字母异位词指字母相同，但排列不同的字符串。
  不考虑答案输出的顺序。
  输入:
s: "cbaebabacd" p: "abc"
输出: [0, 6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
利用滑动窗口，思考一下什么时候移动右指针，什么时候移动左指针。 维护两个字典和一个match常数来判断left到right中是否存在满足的数量。
利用need来保存需要目标子串的所有字符出现次数 利用have来保存当前窗口下的子串的所有字符出现次数 match表示满足字符出现次数的数量 plen表示需要满足字符出现次数的数量
1. 移动right指针，当have[s[right]]==need[s[right]]时，match++
2. 当match==plen且窗口大小等于所需字符数量，保存结果
3. 当match==plen且窗口大小大于所需字符数量，移动left指针，并令对应的have[s[left]]--，如果
have[s[left]] < need[s[left]]，令match-- 4. 重复123步直到right指针到最右边
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left, right, match = 0, 0, 0
        need, have = {}, {}
        for x in p:
            need[x] = need.get(x, 0) + 1
        pset = set(p)
        plen = len(pset)
        window = len(p)
        result = []
        while right < len(s):
        # 先移动right
            if s[right] in pset:
                have[s[right]] = have.get(s[right], 0) + 1
                if have[s[right]] == need[s[right]]:
                  match += 1
            right += 1
        # 再移动left
            while match == plen:
                if right - left == window:
                    result.append(left)
                if s[left] in pset:
                    have[s[left]] = have.get(s[left], 0) - 1
                    if have[s[left]] < need[s[left]]:
                        match -= 1
                left += 1
        return result