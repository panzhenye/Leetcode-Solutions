from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        '''通过两个循环实现换位，matrix里面的数组逐个处理，能行，但效率低'''
        n = len(matrix)
        n2 = len(matrix[0])
        rs = [[] for _ in range(n2)]
        for i in range(0, n):
            for j in range(0, n2):
                rs[j].append(matrix[i][j])
        return rs

    def optimalSolution(self, matrix: List[List[int]]) -> List[List[int]]:
        '''通过两个循环实现换位，matrix里面的数组逐个处理，能行，但效率低'''
        n = len(matrix)
        n2 = len(matrix[0])
        rs = [[] for _ in range(n)]
        for i in range(0, n2):
            j = n - i -abs(n2-n)
            rs[i].append(matrix[j][i])
            rs[j].append(matrix[i][j])
        return rs

        n = len(matrix)
        for i in range(n):
            j=n-i
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6]]
    sol = Solution()
    print(sol.optimalSolution(matrix))
