""" Python script to perform binary search on a list stored in an array """

# Write your code from here

'''
## Method 1 :
## This method is to enter data manually into the array

array = []
b = []
while True:
  a = (input("Enter the integer to append into array to end input press 'end' : "))
  if a == "end" :
    break
  else :
    b.append(a)
for i in b :
  b = int(i)
  array.append(b)
array.sort()
##print(array)

input = int(input("Enter the object to search : "))
while True:
  if len(array) == 1 :
    if array[0] == input :
      print("Object Found")
    else :
      print("Object Not Found")
    break
  b = array[len(array)//2]
  if b == input :
    print("Object Found")
    break
  elif b < input :
    array = array[len(array)//2:]
  else:
    array = array[:len(array)//2]
'''

## Method 2 :
## This method is to take a array with data already included.
## Using random intergers to fill the array by importing random
import random
array = []
a = random.randint(20,51)
for i in range(0,a) :
  b = random.randint(1,50)
  array.append(b)
array.sort()

input = int(input("Enter the Integer to be searched : "))
while True:
  if len(array) == 1 :
    if array[0] == input :
      print("Object Found")
    else :
      print("Object Not Found")
    break
  b = array[len(array)//2]
  if b == input :
    print("Object Found")
    break
  elif b < input :
    array = array[len(array)//2:]
  else:
    array = array[:len(array)//2]  
