""" Python Script to implement various sorting techniques: 
    - Insertion sort
    - Selection Sort
    - Bubble Sort
    - Merge Sort
    - Quick Sort 
    [Compare with Python's Built-In Sorting Functions also]  """

# Write your code from here

def headline(data):
    if data == 1 :
        print("\nOutput of Bubble Sort :\n")
    elif data == 2 :
        print("\nOutput of Quick Sort :\n")
    elif data == 3:
        print("\nOutput of Insertion Sort :\n")
    elif data == 4:
        print("\nOutput of Merge Sort :\n")
    elif data == 5:
        print("\nOutput of Shell Sort :\n")
    elif data == 6:
        print("\nOutput of Selection Sort :\n")


# Python program for implementation of Bubble Sort
def bubble_sort(vals_of_bubble):
    size = len(vals_of_bubble)

    for i in range(size-1):
        swapped = False
        print("Iteration - ", i+1 , "Input list = ", vals_of_bubble)
        for j in range(size-1-i):
            if vals_of_bubble[j] > vals_of_bubble[j+1]:
                tmp = vals_of_bubble[j]
                vals_of_bubble[j] = vals_of_bubble[j+1]
                vals_of_bubble[j+1] = tmp
                swapped = True
        if not swapped:
            break


# implementation of quick sort in python using hoare partition scheme
def swap(a, b, arr):
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def quick_sort(elements, start, end):
    print(elements)
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1, end)

def partition(elements, start, end):
    
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start+=1

        while elements[end] > pivot:
            end-=1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end


# Python program for implementation of Insertion Sort
def insertion_sort(elements):
    for i in range(1, len(elements)):
        print("Iteration - ", i , "Input list = ",elements)
        anchor = elements[i]
        j = i - 1
        while j>=0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j - 1
        elements[j+1] = anchor


# Python program for implementation of Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge_two_sorted_lists(left, right)

def merge_two_sorted_lists(a,b):
    sorted_list = []

    len_a = len(a)
    len_b = len(b)
    i = j = 0
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i+=1
        else:
            sorted_list.append(b[j])
            j+=1
    while i < len_a:
        sorted_list.append(a[i])
        i+=1
    while j < len_b:
        sorted_list.append(b[j])
        j+=1
    return sorted_list


# Python program for implemation of Shell Sort
def shell_sort(arr):
    size = len(arr)
    gap = size//2

    while gap > 0:
        for i in range(gap,size):
            anchor = arr[i]
            j = i
            while j>=gap and arr[j-gap]>anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2

def foo(arr):
    size = len(arr)
    gap = size // 2
    gap = 3
    for i in range(gap, size):
        anchor = arr[i]
        j = i
        while j>=gap and arr[j-gap]>anchor:
            arr[j] = arr[j-gap]
            j -= gap
        arr[j] = anchor


# Python program for implementation of Selection Sort
def selection_sort(arr):
    size = len(arr)
    for i in range(size-1):
        print("Iteration - ", i+1 , "Input list = ",arr)
        min_index = i
        for j in range(min_index+1,size):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == '__main__':
    elements_3 = [11,9,29,7,2,15,28]
    headline(3)
    insertion_sort(elements_3)
    print("Elements after sorting :",elements_3)

    elements_6 = [89, 78, 61, 17, 12, 9, 7, 6, 1]
    headline(6)
    selection_sort(elements_6)
    print("Elements after sorting :",elements_6)

    elements_1 = [5,9,2,1,67,34,88,34]
    headline(1)
    bubble_sort(elements_1)
    print("Elements after sorting :",elements_1)

    elements_4 = [10,3,15,7,8,23,98,29]
    headline(4)
    merge_sort(elements_4)
    print("Elements after sorting :",elements_4)

    elements_2 = [11,9,29,7,2,15,28]
    headline(2)
    quick_sort(elements_2, 0, len(elements_2)-1)
    print("Elements after sorting :",elements_2)

    elements_5 = [89,78,61,53,23,21,17,12,9,7,6,2,1]
    headline(5)
    shell_sort(elements_5)
    print("Elements after sorting :",elements_5)

## OUTPUT :
"""
Output of Insertion Sort :

Iteration -  1 Input list =  [11, 9, 29, 7, 2, 15, 28]
Iteration -  2 Input list =  [9, 11, 29, 7, 2, 15, 28]
Iteration -  3 Input list =  [9, 11, 29, 7, 2, 15, 28]
Iteration -  4 Input list =  [7, 9, 11, 29, 2, 15, 28]
Iteration -  5 Input list =  [2, 7, 9, 11, 29, 15, 28]
Iteration -  6 Input list =  [2, 7, 9, 11, 15, 29, 28]
Elements after sorting : [2, 7, 9, 11, 15, 28, 29]

Output of Selection Sort :

Iteration -  1 Input list =  [89, 78, 61, 17, 12, 9, 7, 6, 1]
Iteration -  2 Input list =  [1, 78, 61, 17, 12, 9, 7, 6, 89]
Iteration -  3 Input list =  [1, 6, 61, 17, 12, 9, 7, 78, 89]
Iteration -  4 Input list =  [1, 6, 7, 17, 12, 9, 61, 78, 89]
Iteration -  5 Input list =  [1, 6, 7, 9, 12, 17, 61, 78, 89]
Iteration -  6 Input list =  [1, 6, 7, 9, 12, 17, 61, 78, 89]
Iteration -  7 Input list =  [1, 6, 7, 9, 12, 17, 61, 78, 89]
Iteration -  8 Input list =  [1, 6, 7, 9, 12, 17, 61, 78, 89]
Elements after sorting : [1, 6, 7, 9, 12, 17, 61, 78, 89]

Output of Bubble Sort :

Iteration -  1 Input list =  [5, 9, 2, 1, 67, 34, 88, 34]
Iteration -  2 Input list =  [5, 2, 1, 9, 34, 67, 34, 88]
Iteration -  3 Input list =  [2, 1, 5, 9, 34, 34, 67, 88]
Iteration -  4 Input list =  [1, 2, 5, 9, 34, 34, 67, 88]
Elements after sorting : [1, 2, 5, 9, 34, 34, 67, 88]

Output of Merge Sort :

Elements after sorting : [10, 3, 15, 7, 8, 23, 98, 29]

Output of Quick Sort :

[11, 9, 29, 7, 2, 15, 28]
[7, 9, 2, 11, 29, 15, 28]
[2, 7, 9, 11, 29, 15, 28]
[2, 7, 9, 11, 29, 15, 28]
[2, 7, 9, 11, 29, 15, 28]
[2, 7, 9, 11, 28, 15, 29]
[2, 7, 9, 11, 15, 28, 29]
[2, 7, 9, 11, 15, 28, 29]
[2, 7, 9, 11, 15, 28, 29]
Elements after sorting : [2, 7, 9, 11, 15, 28, 29]

Output of Shell Sort :

Elements after sorting : [1, 2, 6, 7, 9, 12, 17, 21, 23, 53, 61, 78, 89]
"""
