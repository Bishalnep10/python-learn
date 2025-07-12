"""
Right-Aligned Pyramid:

Write a program that prints a right-aligned pyramid of asterisks with 5 rows:

Copy
    *
   **
  *
 **
***
"""
def right_pyramid(n):
    for i in range(1,n+1):
        for j in range(n+1):
            print(" ", end="")
        for k in range(1,2*i):
            print("*", end="")
        print()

right_pyramid(5)