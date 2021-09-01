""" Python Script to create a stack and perform various operations on it """

# Write your code from here

# Created a empty stack to perform pop and push functions
stack_01 = []

# Inserting data into a list by manual method
print("Enter 'end' to stop appending")
while True :
  data = input("Enter data to append : ")
  stack_01.append(data)
  if data == "end" :
    break
stack_01.pop()
# Stack with the inserted values printed
print('\nStack = ', stack_01)
print()

# The number of elements to be poped out of list
value = int(input("Enter the number of elements to be poped: "))

for i in range(value) :
  stack_01.pop()
print('\nStack after elements are poped :')
# The final stack after poping the elements
print(stack_01)
