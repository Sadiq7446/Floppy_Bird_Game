""" Python Script to find primes numbers upto a specified limit """

# Write your code from here

start = 1
limit = int(input("specify the limit:"))
limit += 1
for i in range(start, limit):
    for j in range(2, i//2):
        if i % j == 0:
            break
    else:
        print(i)

print("These are the primes numbers upto a specified limit")

''' ***OUT PUT***
specify the limit:30
1
2
3
4
5
7
11
13
17
19
23
29
These are the primes numbers upto a specified limit
'''
