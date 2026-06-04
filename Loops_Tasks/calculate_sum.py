# Take input from user and convert to integer
n = int(input("Enter number: "))

# Variable to store the sum
s = 0

# Loop from 1 to n (n+1 is used because range is exclusive)
for i in range(1, n + 1):
    s += i

print("Sum is:", s)
