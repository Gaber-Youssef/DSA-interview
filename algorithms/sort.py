def selection_sort(arr):
    """
    The algorithm repeatedly selects the smallest (or largest) element from the unsorted 
    portion of the list and swaps it with the first element of the unsorted part. 
    This process is repeated for the remaining unsorted portion until the entire list is sorted. 
    
    time complexity: O(n^2)
    is stable: No
    is in-place: Yes
    memory complexity: O(1)
    
    """
    # traverse through all array elements
    for i in range(len(arr)):
        # find the minimum element in remaining unsorted array
        min_index = i
        for j in range(i+1, len(arr)):
            if(arr[j] < arr[min_index]):
                min_index = j
        # swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def bubble_sort(arr):
    """
    The algorithm repeatedly compares adjacent elements and swaps them if they are in the wrong order. 
    This process is repeated for the entire array until the array is sorted.
    
    time complexity: O(n^2)
    is stable: Yes
    is in-place: Yes
    memory complexity: O(1)
    
    """
    # traverse through all array elements
    for i in range(len(arr)):
        # traverse the array from 0 to n-i-1
        # last i elements are already in place
        for j in range(0, len(arr)-i-1):
            # swap if the element found is greater than the next element
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def insertion_sort(arr):
    """
    The algorithm divides the array into two parts: sorted and unsorted. 
    Initially, the sorted part contains only the first element of the array. 
    Then, one by one, elements are picked from the unsorted part and inserted into their correct position in the sorted part. 
    This process is repeated until the entire array is sorted.
    
    time complexity: O(n^2)
    is stable: Yes
    is in-place: Yes
    memory complexity: O(1)
    
    """
    # traverse through all array elements
    for i in range(1, len(arr)):
        key = arr[i]
        # move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        j = i-1
        while(j >= 0 and key < arr[j]):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


def merge_sort(arr):
    """
    The algorithm divides the array into two halves, sorts them recursively, and then merges the two sorted halves.
    
    time complexity: O(nlogn)
    is stable: Yes
    is in-place: No
    memory complexity: O(n)
    
    """
    # divide the array into two halves
    if(len(arr) > 1):
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        # sort the first and second halves
        merge_sort(left)
        merge_sort(right)
        # merge the sorted halves
        i = j = k = 0
        while(i < len(left) and j < len(right)):
            if(left[i] < right[j]):
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        # check if any element was left
        while(i < len(left)):
            arr[k] = left[i]
            i += 1
            k += 1
        while(j < len(right)):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


def quick_sort(arr):
    """
    The algorithm picks a pivot element, rearranges the array elements in such a way that all elements smaller than the picked pivot element move to the left side of the pivot, and all greater elements move to the right side. 
    The same steps are then performed recursively for the left and right sub-arrays.
    
    time complexity: O(nlogn)
    is stable: No
    is in-place: Yes
    memory complexity: O(logn)
    
    """
    # divide the array into two halves
    if(len(arr) > 1):
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if(arr[i] < pivot):
                left.append(arr[i])
            else:
                right.append(arr[i])
        # sort the first and second halves
        quick_sort(left)
        quick_sort(right)
        # merge the sorted halves
        arr[:] = left + [pivot] + right
    return arr