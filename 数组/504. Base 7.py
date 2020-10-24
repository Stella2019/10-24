class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        sign = '' if num >= 0 else '-'
        num = abs(num)
        ans = []
        while num >= 7:
            num, res = divmod(num, 7)
            ans.append(str(res))
        ans.append(str(num))
        return sign +''.join(reversed(ans))