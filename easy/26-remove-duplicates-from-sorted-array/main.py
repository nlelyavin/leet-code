from typing import List


class Solution:

    @staticmethod
    def remove_duplicates(nums: List[int]) -> int:
        insert_index = 1

        for i in range(1, len(nums)):

            if nums[i] != nums[i - 1]:
                nums[insert_index] = nums[i]
                insert_index += 1

        return insert_index


if __name__ == '__main__':
    solution = Solution()
    list_1 = [1, 1, 2]
    solution = solution.remove_duplicates(nums=list_1)
    print(list_1, solution)
