## To run this file you have to install pyshorteners package 
## "pip install pyshorteners" paste this to install the package

import pyshorteners

link = input("Enter the link : ")

shortener = pyshorteners.Shortener()

x = shortener.tinyurl.short(link)

print("\nThe shorten URL is : ",x)


## OUTPUT :
"""
Enter the link : https://learn.gitam.edu/my/

The shorten URL is :  https://tinyurl.com/yh6p7ar6

"""
