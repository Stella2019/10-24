"""
在一个二维数组中(每个一维数组的长度相同)，每一行都按照从左到右递增的顺序排序，每一列都按
照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

利用二维数组由上到下，由左到右递增的规律，那么选取左下角或者右上角的元素
与target进行 比较，当target大于元素
 时，那么target必定在元素a所在行的右边,即j++;当target大于元素
时，那么target必定在元素a所在列的上边,即i--;时间复杂度O(m+n)
"""

class Solution:
# array 二维列表
 def Find(self, target, array):
# write code here
# 用左下角和右上角的数据进行对比，思考一下为什么
    left_row, left_column = len(array) - 1, 0
    right_row, right_column = 0, len(array[0]) - 1
    while left_row >= right_row and left_column <= right_column:
            if array[left_row][left_column] > target:
                left_row -= 1
            elif array[left_row][left_column] < target:
                left_column += 1
            else:
                return True
            if array[right_row][right_column] < target:
                right_row += 1
            elif array[right_row][right_column] > target:
                right_column -= 1
            else:
                return True
    return False