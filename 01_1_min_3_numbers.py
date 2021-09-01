""" Python Script to find minimum among three numbers """

# Write your code from here

# Take input from user 
Num_1 = int(input("Enter your first number : "))
Num_2 = int(input("Enter your Second number : "))
Num_3 = int(input("Enter your third number : "))

''' *** First method *** '''

# 01. Compare Num_1 with Num_2 and Num_3
if Num_1 <= Num_2 and Num_1 <= Num_3 :
  print(Num_1,"is the minimum among three numbers")

# 02. Compare Num_2 with Num_1 and Num_3  
elif Num_2 <= Num_1 and Num_2 <= Num_3 :
  print(Num_2,"is the minimum among three numbers")

# 03. As I compared Num_1 and Num_2 now we can go with 'else' cause it is the only left posibility 
else :
  print(Num_3,"is the minimum among three numbers") 

''' *** Second method ***

if Num_1 <= Num_2 :
  if Num_1 <= Num_3 :
    print(Num_1,"is the minimum among three numbers")
  else :
    print(Num_3,"is the minimum among three numbers")

else:
  if Num_2 <= Num_3 :
    print(Num_2,"is the minimum among three numbers")
  else:
    print(Num_3,"is the minimum among three numbers")
'''
''' *** OUT PUT***
Enter your first number : 548
Enter your Second number : 1000
Enter your third number : 800
548 is the minimum among three numbers
'''
