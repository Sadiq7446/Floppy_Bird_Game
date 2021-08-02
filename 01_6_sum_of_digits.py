""" Python Script to find sum of digits of a number """
# Write your code from here

Numb = int(input("Please Enter a Number: ")) 
i = 0 

while(Numb > 0): 
    a = Numb % 10 
    i = i + a 
    Numb = Numb //10 

print("Sum of the digits of the Given Number =" ,i) 

''' *** OUT PUT ***
Please Enter a Number: 541582
Sum of the digits of the Given Number = 25
>>>
Please Enter a Number: 541
Sum of the digits of the Given Number = 10
'''
