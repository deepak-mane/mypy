# Python Program to Print all the Prime Numbers within a Given Range
# This is a Python Program to print all prime numbers within a given range.
# Problem Description
# The program takes in the upper limit and prints all prime numbers within the given range.
#
# Problem Solution
# 1.	Take in the upper limit for the range and store it in a variable.
# 2.	Let the first for loop range from 2 to the upper limit.
# 3. Initialize the count variable to 0.
# 4.	Let the second for loop range from 2 to half of the number (excluding 1 and the number itself).
# 5.	Then find the number of divisors using the if statement and increment the count variable each time.
# 6. If the number of divisors is lesser than or equal to 0, the number is prime.
# 7. Print the final result.
# 8.	Exit.
#
# Program/Source Code
# Here is source code of the Python Program to check if a number is a prime number. The program output is also shown below.

r=int(input("Enter upper limit: "))
for a in range(2,r+1):
    k=0
    for i in range(2,a//2+1):
        if(a%i==0):
            k=k+1
    if(k<=0):
        print(a)


#
# Program Explanation
# 1.	User must enter the upper limit of the range and store it in a different variable.
# 2. The first for loop ranges till the upper limit entered by the user.
# 3.	The count variable is first initialized to 0.
# 4.	The for loop ranges from 2 to the half of the number so 1 and the number itself aren’t counted as divisors.
# 5.	The if statement then checks for the divisors of the number if the remainder is equal to 0.
# 6. The count variable counts the number of divisors and if the count is lesser or equal to 0, the number is a prime number.
# 7. If the count is greater than 0, the number isn’t prime.
# 8. The final result is printed.
#
# Runtime Test Cases
# Case 1: Enter upper limit: 15
# 2
# 3
# 5
# 7
# 11
# 13
#
# Case 2: Enter upper limit: 40
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19
# 23
# 29
# 31
# 37