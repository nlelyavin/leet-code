from typing import List


class Solution:

    @staticmethod
    def majority_element(nums: List[int]) -> int:
        nums = sorted(nums)
        max_times = 0
        current_times = 0
        majority = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                current_times += 1
            else:
                current_times = 1

            if current_times > max_times:
                majority = nums[i]
                max_times = current_times

        return majority


if __name__ == '__main__':
    solution = Solution()
    list_1 = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
    solution = solution.majority_element(nums=list_1)
    print(list_1, solution)
