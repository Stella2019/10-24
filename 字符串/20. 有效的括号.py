"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        lookup = {"(":")", "{": "}", "[": "]"}
        for parenthese in s:
            if parenthese in lookup:
                stack.append(parenthese)
            #lookup {[]}
            #[{]}
            elif len(stack) == 0 or lookup[stack.pop()] != parenthese:
                return False
            #s = "]"

        return len(stack) == 0




class Solution(object):
  def isValid(self, s):

    parens = {
      '[' : ']',
      '{' : '}',
      '(' : ')',
    }
    inv_parens = {v:k for k,v in parens.items()}

    stack = []
    for c in s:
      if c in parens:
        stack.append(c)
      elif c in inv_parens:
        if len(stack) == 0 or stack[-1] != inv_parens[c]:
          return False
        else:
          stack.pop()
    return len(stack) == 0

print(Solution().isValid('(){([])}'))
# True

print(Solution().isValid('(){(['))
# False