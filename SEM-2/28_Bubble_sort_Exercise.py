"""
Modify bubble_sort function such that it can sort following list of transactions happening in an electronic store,

elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
bubble_sort function should take key from a transaction record and sort the list as per that key.

For example,
bubble_sort(elements, key='transaction_amount')
This will sort elements by transaction_amount and your sorted list will look like,

elements = [
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
    ]
"""

## Code from here

def bubble_sort(elements, key=None):
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            a = elements[j][key]
            b = elements[j+1][key]
            if a > b:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True

        if not swapped:
            break

if __name__ == '__main__':
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
    key = input("Enter the input for key: ")
    bubble_sort(elements, key)
    print(elements)

## OUTPUT:
"""
## INPUT as name 

[{'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'}, 
 {'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'}, 
 {'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'}, 
 {'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'}]

## INPUT as transaction_amount

[{'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'}, 
 {'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'}, 
 {'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'}, 
 {'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'}]

## INPUT as device

[{'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'}, 
 {'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'}, 
 {'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'}, 
 {'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'}]
"""
