""" Python Script to find GCD and LCM of 3 numbers """

# Write your code from here


import math

a=int(input("Enter your 1st number : "))
b=int(input("Enter your 2nd number : "))
c=int(input("Enter your 3rd number : "))

G_abc = math.gcd(math.gcd(a,b),c)
G_ab = math.gcd(a,b)
G_ac = math.gcd(a,c)
G_bc = math.gcd(b,c)

L_abc = int((a*b*c*G_abc)/(G_ab*G_bc*G_ac))

print("GCD of",a,",",b,",",c,"is",G_abc)
print("LCM of",a,",",b,",",c,"is",L_abc)

''' ***Out Put***
Enter your 1st number : 5
Enter your 2nd number : 10
Enter your 3rd number : 20
GCD of 5 , 10 , 20 is 5
LCM of 5 , 10 , 20 is 20  
'''
