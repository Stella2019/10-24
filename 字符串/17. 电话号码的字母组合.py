class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.keys = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        combinations, prefix = [], ""
        if not digits:
            return combinations
        self.doCombinations(prefix, combinations, digits)
        return combinations

    def doCombinations(self, prefix: str, combinations: List[str], digits: str):
        if len(prefix) == len(digits):
            combinations.append(prefix)
            return
        for i in self.keys[int(digits[len(prefix)])]:
            prefix += i
            self.doCombinations(prefix, combinations, digits)
            prefix = prefix[:-1]







lettersMaps = {
    1: [],
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
    0: []
}

validWords = ['dog', 'fish', 'cat', 'fog']


def makeWords_helper(digits, letters):
  if not digits:
    word = ''.join(letters)
    if word in validWords:
      return [word]
    return []

  results = []
  chars = lettersMaps[digits[0]]
  for char in chars:
    results += makeWords_helper(digits[1:], letters + [char])
  return results


def makeWords(phone):
  digits = []
  for digit in phone:
    digits.append(int(digit))
  return makeWords_helper(digits, [])


print(makeWords('364'))