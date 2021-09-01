"""
Implement quick sort using lumoto partition scheme.
"""

## Code from here

# This implements quick sort using lomuto partition scheme
def swap(a, b, arr):
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def quick_sort(elements, start, end):
    if len(elements)== 1:
        return
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1, end)

def partition(elements, start, end):
    pivot = elements[end]
    p_index = start

    for i in range(start, end):
        if elements[i] <= pivot:
            swap(i, p_index, elements)
            p_index += 1

    swap(p_index, end, elements)

    return p_index


if __name__ == '__main__':
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        print(f"\nBefore sorting: {elements}")
        quick_sort(elements, 0, len(elements)-1)
        print(f"after sorting: {elements}")

## OUTPUT 
"""
Before sorting: [11, 9, 29, 7, 2, 15, 28]
after sorting: [2, 7, 9, 11, 15, 28, 29]

Before sorting: [3, 7, 9, 11]
after sorting: [3, 7, 9, 11]

Before sorting: [25, 22, 21, 10]
after sorting: [10, 21, 22, 25]

Before sorting: [29, 15, 28]
after sorting: [15, 28, 29]

Before sorting: []
after sorting: []

Before sorting: [6]
after sorting: [6]
"""
