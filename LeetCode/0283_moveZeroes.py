from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        记录值为0的index，然后从后往前删，再append一个0
        """
        remove_list = []
        for index, s in enumerate(nums):
            if s == 0:
                remove_list.append(index)
        for i in remove_list[::-1]:
            del nums[i]
            nums.append(0)

    def optimalSolution(self, nums: List[int]) -> None:
        '''
        用另外一个数组去存非0的数据，然后记录有多少个0，加上去。
        '''
        result = []
        count = 0
        for s in nums:
            if s != 0:
                result.append(s)
            else:
                count += 1
        result.extend([0] * count)
        nums[:] = result

    def officialSolution(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
            print(nums)


if __name__ == '__main__':
    s = Solution()

    nums = [0, 1, 0, 3, 12]
    s.moveZeroes(nums)
    print(nums)

    nums = [0, 1, 0, 3, 12]
    s.optimalSolution(nums)
    print(nums)

    nums = [0, 1, 0, 3, 12]
    s.officialSolution(nums)
    print(nums)
