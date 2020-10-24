class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i = 0
        j = 0
        res = 0
        while i < len(g) and j < len(s):
            if s[j] < g[i]:
                j += 1
            else:
                i += 1
                j += 1
                res += 1
        return res