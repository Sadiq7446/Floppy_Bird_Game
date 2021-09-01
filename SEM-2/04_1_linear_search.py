""" Python script to perform linear search in an array. """

# Write your code from here

'''
## Method 1 :
## This method is to enter data manually into the array

array = []
while True:
  a = input("Enter the input to append into array to end input press 'end' : ")
  if a == "end" :
    break
  else :
    array.append(a)
c = 0
b = input("Enter the object to search : ")
for i in array:
  if b == i :
    print("object Found.")
    c = 1
    break
if c == 0 :
  print("Object Not Found.") 
'''

## Method 2 :
## This method is to take a array with data already included.
## Using random intergers to fill the array by importing random
import random
array = []
a = random.randint(1,51)
for i in range(0,a):
  b = random.randint(1,1000)
  array.append(b)

c = int(input("Enter the integer to be searched : "))
d = 0
for j in array :
  if j == c :
    print("Found The Integer")
    d = 1
    break
if d == 0 :
  print ("Integer Not Found")
