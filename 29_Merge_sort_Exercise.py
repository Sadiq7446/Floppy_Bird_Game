"""
Modify merge_sort function such that it can sort following list of athletes as per the time taken by them in the marathon,

elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
merge_sort function should take key from an athlete's marathon log and sort the list as per that key.
"""

## Code from here

def merge_sort(elements, key, descending=False):
    size = len(elements)

    if size == 1:
        return elements

    left_list = merge_sort(elements[0:size//2], key, descending)
    right_list = merge_sort(elements[size//2:], key, descending)
    sorted_list = merge(left_list, right_list, key, descending)

    return sorted_list

    
def merge(left_list, right_list, key, descending=False):
    merged = []
    if descending:
        while len(left_list) > 0 and len(right_list) > 0:
            if left_list[0][key] >= right_list[0][key]:
                merged.append(left_list.pop(0))
            else:
                merged.append(right_list.pop(0))

    else:
        while len(left_list) > 0 and len(right_list) > 0:
            if left_list[0][key] <= right_list[0][key]:
                merged.append(left_list.pop(0))
            else:
                merged.append(right_list.pop(0))

    merged.extend(left_list)
    merged.extend(right_list)
    return merged

if __name__ == '__main__':
    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
    key = input("Enter the key to sort : ")
    sorted_list = merge_sort(elements, key, descending=True)
    print(sorted_list)

## OUTPUT
"""
## INPUT as name
[{'name': 'vignesh', 'age': 21, 'time_hours': 2.5}, 
 {'name': 'vedanth', 'age': 17, 'time_hours': 1}, 
 {'name': 'rajab', 'age': 12, 'time_hours': 3}, 
 {'name': 'chinmay', 'age': 24, 'time_hours': 1.5}]

## INPUT as age
[{'name': 'chinmay', 'age': 24, 'time_hours': 1.5}, 
 {'name': 'vignesh', 'age': 21, 'time_hours': 2.5}, 
 {'name': 'vedanth', 'age': 17, 'time_hours': 1}, 
 {'name': 'rajab', 'age': 12, 'time_hours': 3}]

## INPUT as time_hours 
[{'name': 'rajab', 'age': 12, 'time_hours': 3}, 
 {'name': 'vignesh', 'age': 21, 'time_hours': 2.5}, 
 {'name': 'chinmay', 'age': 24, 'time_hours': 1.5}, 
 {'name': 'vedanth', 'age': 17, 'time_hours': 1}]
"""
