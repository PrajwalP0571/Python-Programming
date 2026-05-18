# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/

# Exercise 1. Print first 10 natural numbers using while loop

n = 1
while n<=10:
    print(n)
    n += 1

print("----------Task 1--------------")
# Exercise 2. Display numbers from -10 to -1 using for loop

for i in range(-10,0):
    print(i)
    i += 1

print("----------Task 2--------------")

# Exercise 3. Display a message “Done” after successful execution of for loop

for i in range(1,5):
    print(i)
    i+=1
print("Done!")

print("----------Task 3--------------")

# Exercise 4. Calculate the sum of all numbers from 1 to N

print("Enter a number: ")
n = 5

sum = n*(n+1)/2
print(int(sum))

print("----------Task 4--------------")

# Exercise 5. Print multiplication table of a given number

number = 2

for i in range(1,11):
    print(f"{number} X {i} = {number * i}")

print("----------Task 5--------------")

# Exercise 6. Calculate the cube of all numbers from 1 to a given number

n = 5

for i in range(1,n):
    print(f"Cube of {i} = {i*i*i} ")

print("----------Task 6--------------")

# Exercise 7. Display numbers from a list using a loop
'''
The number must be divisible by five.
If the number is greater than 150, skip it and move to the next.
If the number is greater than 500, stop the loop entirely.
'''

numbers = [12, 75, 150, 180, 145, 525, 50]

for i in range(0,len(numbers)):
    if numbers[i] > 500:
            break
    if numbers[i] %  5 == 0:
        if numbers[i] > 150:
            continue
        else:
            print(numbers[i])
        

print("----------Task 7--------------")

# Exercise 8. Count occurrences of a specific element in a list

list1 = [10, 20, 10, 30, 10, 40, 50]
target = 10
count = 0

for i in range(0,len(list1)):
    if list1[i] == 10:
        count +=1
print(f"The Number {target} occurs {count} times in the list1")

print("----------Task 8--------------")

# Exercise 9. Print elements from a list present at odd index positions

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(1,len(my_list),2):
    print(my_list[i], end=" ")

print(" ")

print("----------Task 9--------------")

# Exercise 10. Print list in reverse order using a loop

list1 = [10, 20, 30, 40, 50]

for i in reversed(list1):
    print(i)

print("----------Task 10--------------")

# Exercise 11. Reverse a string using a for loop (no slicing)

str = "Python"
rev_str = ""

for char in str:
    rev_str = char + rev_str
print(rev_str)

print("----------Task 11--------------")


# Exercise 12. Count vowels and consonants in a sentence

sent = "Python is greate"
vovels = "aeiouAEIOU"
v_count = 0
c_count = 0

for char in sent:
    if char.isalpha():
        if char in vovels:
            v_count += 1
        else:
            c_count += 1

print(v_count)
print(c_count)    

#print(f"There are total {vovels} Vovels in the sentence and {consonants} Consonants")

print("----------Task 12--------------")

# Exercise 13. Count total number of digits in a number

num = 78364
count = 0

num = num // 10
while num != 0:
    count+=1
print(count)
# Exercise 14. Reverse an integer number

print("----------Task 13--------------")

# Exercise 14. Reverse an integer number

num = 1234
rev_num = 0

while num != 0:
    num = num % 10
    
print(rev_num)


print("----------Task 14--------------")

# Exercise 15. Find largest and smallest digit in a number

num = 36478


        
print("----------Task 15--------------")


