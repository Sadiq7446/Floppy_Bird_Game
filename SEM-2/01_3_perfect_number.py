""" Python Script to check whether a given number is perfect  """

# Write your code from here
Numb = int(input(" Please Enter any Num: ")) 
a = 0 

for i in range(1, Numb): 
    if(Numb % i == 0): 
        a = a + i 

if (a == Numb): 
    print(Numb,"is a Perfect Number") 
else: 
    print(Numb,"is not a Perfect Number") 

    ''' *** OUT PUT ***
 Please Enter any Num: 6
6 is a Perfect Number

 Please Enter any Num: 9
9 is not a Perfect Number

 Please Enter any Num: 25
25 is not a Perfect Number
'''
