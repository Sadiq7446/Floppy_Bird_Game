""" Python Script to find GCD and LCM of 2 numbers """

# Write your code from here
a=int(input("Enter your first number : "))
b=int(input("Enter your second number : "))

'''GCD'''
a1=a
b1=b
while a1>0 :
    a2=a1
    a1=b1%a1
    b1=a2
    
print("The GCD of",a,"and",b,"is : ",b1)

'''LCM'''

lcm = (a / b1)* b
lcm = int(lcm)

print("The LCM of",a,"and",b,"is : ",lcm)

''' *** OUT PUT ***
Enter your first number : 33
Enter your second number : 54
The GCD of 33 and 54 is :  3
The LCM of 33 and 54 is :  594 
'''
