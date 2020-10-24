"""给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出:包含 T 所有字母的最小子串。
输入: S = "ADOBECODEBANC", T = "ABC" 输出: "BANC"
用滑动窗口的思想就很简单了
1. 初始，left指针和right指针都指向S的第一个元素.
2. 将 right指针右移，扩张窗口，直到得到一个可行窗口，亦即包含TT的全部字母的窗口。 3. 得到可行的窗口后，将left指针逐个右移，若得到的窗口依然可行，则更新最小窗口大小。 4. 若窗口不再可行，则跳转至 2。


"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right, match = 0, 0, 0
        need, have = {}, {}
        result = ""
        result_len = len(s) + 1
        for x in t:
            need[x] = need.get(x, 0) + 1
        tset = set(t)
        match_len = len(need.keys())
        while right < len(s):
            if s[right] in tset:
                have[s[right]] = have.get(s[right], 0) + 1
                if have[s[right]] == need[s[right]]:
                    match += 1
            right += 1
            while match == match_len:
                if right - left < result_len:
                    result = s[left:right]
                    result_len = len(result)
                if s[left] in tset:
                    have[s[left]] = have.get(s[left], 0) - 1
                    if have[s[left]] < need[s[left]]:
                        match -= 1
                left += 1
        return result