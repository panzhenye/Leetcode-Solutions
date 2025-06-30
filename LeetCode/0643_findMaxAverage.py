from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        '''
        定向滑窗的简单题，维护好max_count，对比一头一尾就可以了
        '''
        count = 0
        current = sum(i for i in arr[:k])
        count += (1 if current / k >= threshold else 0)
        for i in range(k, len(arr)):
            current += arr[i] - arr[i - k]
            count += (1 if current / k >= threshold else 0)
        return count


if __name__ == '__main__':
    arr = [2, 2, 2, 2, 5, 5, 5, 8]
    k = 3
    threshold = 4
    sol = Solution()
    print(sol.numOfSubarrays(arr, k, threshold))
