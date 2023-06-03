"""BLANK 1"""

# len_result_list = n + m
# current_num = 100000000000000000
# index_nums_2 = 0 if n else -1
# i = 0
#
# # while (i < len_result_list) and (index_nums_2 >= 0):
#     print(nums1)
#     print(current_num)
#     print(nums2[index_nums_2])
#
#     if i > m - 1:
#         if current_num < nums2[index_nums_2] and current_num != 0:
#             save_num = nums1[i]
#             nums1[i] = current_num
#             current_num = save_num
#         else:
#             # current_num = nums1[i]
#             nums1[i] = nums2[index_nums_2]
#             index_nums_2 += 1
#
#     # Если нужно вставлять элемент из второго массива в первый (мердж)
#     elif (nums1[i] > nums2[index_nums_2]) and n > index_nums_2:
#         if current_num < nums2[index_nums_2]:
#             save_num = nums1[i]
#             nums1[i] = current_num
#             current_num = save_num
#         else:
#             current_num = nums1[i]
#             nums1[i] = nums2[index_nums_2]
#             index_nums_2 += 1
#
#     i += 1
# print(nums1)

"""BLANK 2"""
# while i >= 0 and n:
#     if i == 0:
#         if m == 0:
#             nums1[i] = nums2[i_2]
#         else:
#             nums1[i] = nums1[i_1] if nums1[i_1] < nums2[i_2] else nums2[i_2]
#         i -= 1
#         continue
#
#     if nums1[i_1] > nums2[i_2]:
#         nums1[i] = nums1[i_1]
#         i_1 -= 1 if i_1 > 0 else 0
#     else:
#         nums1[i] = nums2[i_2]
#         i_2 -= 1
#
#     i -= 1