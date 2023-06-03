from typing import List


class Solution:
    @staticmethod
    def remove_element(nums: List[int], val: int) -> int:
        save_index = 0

        for i in range(len(nums)):
            current_value = nums[i]

            if current_value != val:
                nums[i] = val
                nums[save_index] = current_value
                save_index += 1

        return save_index


if __name__ == '__main__':
    solution = Solution()
    list_1 = [0, 1, 2, 2, 3, 0, 4, 2]
    solution = solution.remove_element(nums=list_1, val=2)
    print(list_1)
