from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = n + m - 1
        i_1 = m - 1
        i_2 = n - 1

        while i >= 0:
            if i_2 >= 0:
                if i_1 >= 0 and nums1[i_1] > nums2[i_2]:
                    nums1[i] = nums1[i_1]
                    i_1 -= 1
                else:
                    nums1[i] = nums2[i_2]
                    i_2 -= 1
            else:
                nums1[i] = nums1[i_1]
                i_1 -= 1
            i -= 1


if __name__ == '__main__':
    solution = Solution()
    list_1 = [0, 2, 3, 0, 0, 0, 0]
    list_2 = [-100, 1, 2, 10]
    solution.merge(nums1=list_1, m=len(list_1) - len(list_2), nums2=list_2, n=len(list_2))
    # print(list_1)
