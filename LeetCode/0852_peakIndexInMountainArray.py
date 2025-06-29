from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        i = 0
        while arr[i] < arr[i + 1]:
            i += 1
        return i


if __name__ == '__main__':
    arr = [0, 10, 5, 2]
    sol = Solution()
    print(sol.peakIndexInMountainArray(arr))
