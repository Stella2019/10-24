class Solution(object):
  def uniquePaths(self, m, n):
    if m == 1 or n == 1:
      return 1
    return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)

  def uniquePathsDP(self, m, n):
    cache = [[0] * n] * m
    for i in range(m):
      cache[i][0] = 1
    for j in range(n):
      cache[0][j] = 1

    for c in range(1, m):
      for r in range(1, n):
        cache[c][r] = cache[c][r-1] + cache[c-1][r]
    return cache[-1][-1]

print(Solution().uniquePaths(5, 3))
# 15

print(Solution().uniquePathsDP(5, 3))
# 15