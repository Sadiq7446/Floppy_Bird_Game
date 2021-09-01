""" Python Script to convert the infix expression into postfix form. """

# Write your code from here

## Infix notation is characterized by the placement of operator between the operands like 2 + 2.
## Postfix notation is characterized by the placement of operator after the operands like 2 2 +.
## Prefix notation is characterized by the placement of operator before the operands like + 2 2.

# creating a set of functions that can be used
operator_set = set(['+','-','*','/','(',')','^'])
# taking input from user in infix expression
input = input("Enter the infix expression : ")
# converting input into list
lst = []
for i in input:
  lst.append(i)

# remove functions from lst and add into another list
temp = []
for a in lst:
  if a in operator_set :
    temp.append(a)
    lst.remove(a)

# inserting the funtions from another list to lst at end
int = len(lst)
for b in temp:
    lst.insert(int,b)
    int += 1

# converting list into String
strng = ''
for c in lst :
  strng += c

print("The postfix is :\n",strng)
