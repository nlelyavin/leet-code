from typing import List, Union

REPLACE_SYMBOL = '_'


class Solution:
    @staticmethod
    def remove_duplicates(nums: List[Union[str, int]]) -> int:
        insert_index = 1
        current_offset = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                nums[insert_index] = nums[i]
                current_offset += 1

                if current_offset < 3:
                    insert_index += 1
            else:
                nums[insert_index] = nums[i]
                insert_index += 1
                current_offset = 1

        return insert_index


if __name__ == '__main__':
    solution = Solution()
    list_1 = [1, 1, 1, 2, 2, 2, 3, 3]
    solution = solution.remove_duplicates(nums=list_1)
    print(list_1, solution)
