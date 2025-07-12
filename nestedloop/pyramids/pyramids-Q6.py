"""
Diamond Shape:

Use nested loops to create a diamond shape made of asterisks. The diamond should have 5 rows at its widest point:
markdown

Copy
    *
   *
  ***
 *****
*******
 *****
  ***
   *
"""
def full_pyramid(n):
    for i in range(1,n+1):
        for j in range(n):
            print(" ", end="")
        for k in range(1,2*i):
            print("*", end="")
        print()

full_pyramid(5)
