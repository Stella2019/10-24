"""
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
（注意：规定B[0] = A[1] * A[2] * ... * A[n-1]，B[n-1] = A[0] * A[1] * ... * A[n-2];）
对于A长度为1的情况，B无意义，故而无法构建，因此该情况不会存在。
"""



class Solution:
    def multiply(self, A):
        # write code here
        B1, B2 = [1] * len(A), [1] * len(A)
        for i in range(len(A)-1):
            B1[i+1] = B1[i] * A[i]
        for i in range(len(A)-2, -1, -1):
            B2[i] = B2[i + 1] * A[i + 1]
        B = [1] * len(A)
        for i in range(len(A)):
            B[i] = B1[i] * B2[i]
        return B