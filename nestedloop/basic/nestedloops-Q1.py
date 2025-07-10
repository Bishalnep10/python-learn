"""
Basic Square:

Write a program that prints a square of asterisks (*) with 3 rows and 3 columns:

Copy
*
*
*
"""
num_rows = 3
num_cols = 3

for i in range(num_rows):
    for j in range(num_cols):
        print("*", end="  ")
    print()