"""
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
 

示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2：

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

动态规划：
dp[i][j] 代表 word1 到 i 位置转换成 word2 到 j 位置需要最少步数

所以，

当 word1[i] == word2[j]，dp[i][j] = dp[i-1][j-1]；

当 word1[i] != word2[j]，dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

其中，dp[i-1][j-1] 表示替换操作，dp[i-1][j] 表示删除操作，dp[i][j-1] 表示插入操作。

注意，针对第一行，第一列要单独考虑，我们引入 '' 下图所示：



第一行，是 word1 为空变成 word2 最少步数，就是插入操作

第一列，是 word2 为空，需要的最少步数，就是删除操作

再附上自顶向下的方法，大家可以提供 Java 版吗？


"""

import functools
class Solution:
    @functools.lru_cache(None)
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return len(word1) + len(word2)
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        else:
            inserted = 1 + self.minDistance(word1, word2[1:])
            deleted = 1 + self.minDistance(word1[1:], word2)
            replace = 1 + self.minDistance(word1[1:], word2[1:])
            return min(inserted, deleted, replace)


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        import functools
        @functools.lru_cache(None)
        def helper(i, j):
            if i == len(word1) or j == len(word2):
                return len(word1) - i + len(word2) - j
            if word1[i] == word2[j]:
                return helper(i + 1, j + 1)
            else:
                inserted = helper(i, j + 1)
                deleted = helper(i + 1, j)
                replaced = helper(i + 1, j + 1)
                return min(inserted, deleted, replaced) + 1

        return helper(0, 0)

解题思路
看题目，这应该是一道典型的双字符串动态规划类题目，跟最长递增子序列题套路相似，但又不完全一致。
解题的关键在于理解这三个操作是如何影响规划的动态变化的

定义：dist[i][j]为word1[:i]与word2[:j]完成转换的最小编辑距离，两个字符各增加一个字符，则根据新字符是否相等，有如下情形：

若word1[i] == word2[j]，新字符相等，无需增加编辑距离即可直接转换，即dist[i+1][j+1] = dist[i][j]

若两字符不相等，对最后一次采取何种操作分析如下：

插入，最后操作是对word1插入1个字符，意味着word2[j]由word1中新插入的字符对应，这是在word1[:i+1]和word2[:j]完成转换基础上增加一次插入操作实现，即dist[i+1][j+1] = dist[i+1][n] + 1

删除，最后操作是对word1删除1个字符，意味着删掉word1[i]后两单词匹配，也就是在word1[:i]和word2[:j+1]完成转换的基础上增加一次删除操作实现，即dist[i+1][j+1] = dist[i][j+1] + 1

替换，最后操作是对word1替换1个字符，意味着word1[i]替换成word2[j]后实现两单词匹配，即在word1[:i]和word2[:j]完成转换基础上增加一次替换操作实现，即dist[i+1][j+1] = dist[i][j] + 1

根据动态规划的套路，选择dist[i+1][j+1]的最小值必然是三者取最小，从而有转移方程：dist[i+1][j+1] = min(dist[i+1][j], dist[i][j+1], dist[i][j]) + 1

注意事项：

dist[i][j]是指完成word1前i个字符和word2前j个字符转换的距离，对应的是word1[:i] vs word2[:j]，包括i=0或j=0时，此时一个单词为空，退化为纯插入或纯删除来完成转换，构成初始状态

实际上，定义了dist矩阵后，发现每个方格距离仅与其左、上、左上三个值有关，进而又可以仅定义一个一维距离列表和一个辅助列表实现记录，从而优化空间复杂度

进一步地，考虑定义的三种操作构成对称关系：在word1中删除字符与在word2中插入字符其转换效果是一致的，而替换更是对称操作，从而由word1转换为word2和由word2转换为word1其最小编辑距离也是一致的。基于此，可根据word1和word2字符长短进一步优化空间复杂度为最小的那个维度


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word2)<len(word1):#保证word1是短单词
            word1, word2 = word2, word1
        m, n = len(word1), len(word2)
        dist = list(range(m+1))#word2长度为0时，由不同长度word1转换的编辑距离
        for i in range(1, n+1):
            tmp = [i]*(m+1)#word2长度为i时，由0长度的word1转换的编辑距离
            for j in range(1, m+1):
                if word1[j-1] == word2[i-1]:
                    tmp[j] = dist[j-1]
                else:
                    tmp[j] = min(tmp[j-1], dist[j], dist[j-1]) + 1
            dist = tmp
        return dist[-1]

 





int minDistance(String s1, String s2) {
    int m = s1.length(), n = s2.length();
    int[][] dp = new int[m + 1][n + 1];
    // base case
    for (int i = 1; i <= m; i++)
        dp[i][0] = i;
    for (int j = 1; j <= n; j++)
        dp[0][j] = j;
    // 自底向上求解
    for (int i = 1; i <= m; i++)
        for (int j = 1; j <= n; j++)
            if (s1.charAt(i-1) == s2.charAt(j-1))
                dp[i][j] = dp[i - 1][j - 1];
            else
                dp[i][j] = min(
                    dp[i - 1][j] + 1,
                    dp[i][j - 1] + 1,
                    dp[i-1][j-1] + 1
                );
    // 储存着整个 s1 和 s2 的最小编辑距离
    return dp[m][n];
}

int min(int a, int b, int c) {
    return Math.min(a, Math.min(b, c));
}
