"""在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。
也不知道每个数字重复几次。请找出数组中任意一个重复的数字。
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
把数组中的每个值放到对应的下标的位置上。(数归其标)
1.从头到尾依次扫描这个数组中的每个数字
2.当扫描下标为i的数字时，首先比较这个数字(用m表示)是 不是等于i
3.如果是，则接着扫描下一个数字，如果不是，则再拿它和第m个数字进行比较。
 4.如果它 和第m个数字相等，就找到一个重复的数字(该数字在下标i和m的位置都出现了);
  5.如果它和第m个 数字不相等，就把第i个数字和第m个数字交换，把m放到属于它的位置
  6.重复比较交换过程，直到我们 发现一个重复的数字"""
# -*- coding:utf-8 -*-
class Solution:
# 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
# 函数返回True/False
 def duplicate(self, numbers, duplication):
     i=0
     while i < len(numbers):
            if numbers[i] == i:
                i += 1
                continue
            else:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                temp = numbers[i]
                numbers[i], numbers[temp] = numbers[temp], numbers[i]
     return False