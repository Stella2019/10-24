"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例：

输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]

"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #递归
        if n == 0:
            return []
        result = []
        self.helper(n, n, '', result)
        return result

    def helper(self, l, r, item, result): #l左括号，r右括号个数，item中间值
        if r < l:
            return
        if l == 0 and r == 0:
            result.append(item)
        if l > 0:
            self.helper(l-1, r, item + '(', result)
        if r > 0:
            self.helper(l, r-1, item + ')', result)





class Solution(object):
  def _genParensHelper(self, n, left, right, str):
    if left + right == 2 * n:
      return [str]

    result = []
    if left < n:
      result += self._genParensHelper(n, left + 1, right, str+'(')

    if right < left:
      result += self._genParensHelper(n, left, right + 1, str+')')
    return result

  def genParens(self, n):
    return self._genParensHelper(n, 0, 0, '')


print(Solution().genParens(3))
# ['((()))', '(()())', '(())()', '()(())', '()()()']