from collatz import *

printIntro()

num = int(input("Enter a starting number (greater than 0) or QUIT:\n"))

while num <= 0:
    print("Please input a valid starting number.")
    num = int(input("Enter a starting number (greater than 0) or QUIT:\n"))

print("\nThe sequence is: " + performFormula(num))