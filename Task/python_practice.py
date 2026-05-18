# function to add two numbers
def add(a, b):
    return a + b

# initializing numbers
a = 10
b = 5

# calling function
res = add(a,b)

print(res)


print("===================")

a = 7
b = 3

if a > b:
    print(a)
else:
    print(b)

print("=================")

import math

n = 6
print(math.factorial(n))

print("==================")

def fun(p, t, r):
    return (p * t * r) / 100

p, t, r = 8, 6, 8

res = fun(p, t, r)
print(res)

print("=================")

P = 1200   
R = 5.4    
T = 2      

A = P * (1 + R/100) ** T
CI = A - P

print("Compound interest:", CI)
