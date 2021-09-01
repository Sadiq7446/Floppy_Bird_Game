""" Python Script to find whether a number is armstrong or not """
# Write your code from here
Numb = int (input ("Enter a Number: ")) 
i = 0 

a = Numb 
while a > 0: 
   b = a % 10 
   i += b ** 3 
   a //= 10 

if Numb == i: 
   print(Numb,"is an Armstrong Number") 
else: 
   print(Numb,"is not an Armstrong Number")

    
''' ***OUT PUT***
Enter a Number: 153
153 is an Armstrong Number
>>>
Enter a Number: 548
548 is not an Armstrong Number
'''
