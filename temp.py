# def mergeSort(arr):
#     if len(arr) > 1:
#         mid = len(arr)//2
#         left = arr[:mid]
#         right = arr[mid:]
#
#         mergeSort(left)
#         mergeSort(right)
#
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 arr[k] = left[i]
#                 i = i+1
#             else:
#                 arr[k] = right[j]
#                 j = j+1
#             k = k+1
#
#         while i < len(left):
#             arr[k] = left[i]
#             i = i+1
#             k = k+1
#
#         while j < len(right):
#             arr[k] = right[j]
#             j = j+1
#             k = k+1
#         print(*arr)
#
# list = [7,5,7,54,68,5,7,9,2,53,7]
# mergeSort(list, 0, len(list)-1)
# print(list)
def update(self, index_left, move, start, move, move2, list)
