def quick_sort(ary):
    return qsort(ary,0,len(ary)-1)

def qsort(ary,left,right):
    # Quick row function, ary to sort the array, left to be sorted to the left border, right for the right border
    if left >= right:
        return ary      # If the array is empty or only one element
    key = ary[left]     # Take the leftmost as the baseline
    smaller = left           # left pointer
    greater = right          # right pointer
    i = left
    while i < greater + 1:  # greater is the new position that needs to be taken into account
        if ary[i] < key:
            ary[i], ary[smaller] = ary[smaller], ary[i]
            smaller += 1  # red index move forward
            i += 1  # i move forward, only concern about if i position is smaller. This time is not smaller, so directly move one step
        elif ary[i] > key:
            ary[i], ary[greater] = ary[greater], ary[i]
            greater -= 1  # blue index move forward.
            # don't move i! since now nums[i] could be 0(smaller than the item before it) or 1, this item needs to be judged again.
            # At this time although not greater, but there may be smaller, may be behind key, so also need modification, do not move
        else:
            i += 1
    ary[left],ary[smaller] = ary[smaller],ary[left]    # left and right after all the exchange, the left border left and the left of the number of exchange
    print left,smaller,greater
    qsort(ary,left,smaller-1)    # left interval to do the same sort
    qsort(ary,smaller+1,right)   # right interval to do the same sort
    return ary
print quick_sort([1,3,2,5,6,4])
