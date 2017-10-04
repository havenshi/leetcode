# def qsort_py(items):
#     sort(items, 0, len(items) - 1)
#     return items
#
# def sort(items, left, right):
#     if left >= right:
#         return
#
#     pivot = partition(items, left, right)
#     sort(items, left, pivot - 1)
#     sort(items, pivot + 1, right)
#
# def partition(items, lo, hi):
#     left = lo + 1
#     right = hi
#     while True:
#
#         while items[left] < items[lo]:
#             # find item on left to swap
#             left += 1
#             if left >= hi:
#                 break
#
#         while items[right] > items[lo]:
#             # find item on right to swap
#             right -= 1
#             if right <= lo:
#                 break
#
#         # if we have already gone through all items
#         if left >= right:
#             break
#
#         # swap items
#         items[left], items[right] = items[right], items[left]
#
#     # swap partitioning item with the biggest on the left side (which is less than lo)
#     items[lo], items[right] = items[right], items[lo]
#     return right

def qsort_3w(array):
    return sort_3w(array, 0, len(array) - 1)

def sort_3w(array, left, right):
    if left >= right:
        return
    smaller = left
    greater = right
    pivot = array[left]
    i = left
    while i <= greater: # greater is the new position that needs to be taken into account
        if array[i] < pivot:
            array[smaller], array[i] = array[i], array[smaller] # swap
            smaller += 1 # smaller index move forward
            i += 1
        elif array[i] > pivot:
            array[greater], array[i] = array[i], array[greater] # swap
            greater -= 1 # greater index move forward
            # don't move i! since now nums[i] could be smaller than pivot, this item needs to be judged again.
        else:
            i += 1
    sort_3w(array, left, smaller - 1)
    sort_3w(array, greater + 1, right)
    return array

print qsort_3w([1,3,2,5,6,4])