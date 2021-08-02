""" Python Script to find twin primes upto a specified limit """

# Write your code from here

def Prime(n):  

   for i in range(2, n):  
      if n % i == 0:  
         return False  
   return True  

def Twins_prime(one, limit):  
   for i in range(one, limit):  
      j = i + 2  
      if(Prime(i) and Prime(j)):  
         print(i,'and',j)  

Twins_prime(1,int(input("Specify the limit : "))) 

'''***OUTPUT***
Specify the limit : 100
1 and 3
3 and 5
5 and 7
11 and 13
17 and 19
29 and 31
41 and 43
59 and 61
71 and 73
'''
