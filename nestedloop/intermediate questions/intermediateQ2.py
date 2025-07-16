"""
Diamond Pattern:

Create a program that prints a diamond shape with 5 rows at the widest point:

Copy
  *
 *
***
 *
  *
"""
def print_diamond(rows):
    for i in range(rows):
        for j in range(rows - i - 1):
            print(" ",end="")
        for k in range(2 * i + 1):
            print("*",end="")
        print()
    for i in range(rows - 2 , - 1 , - 1):
        print("",end="")
        for j in range(rows - i - 1):
            print(" ",end="")
        for k in range(2 * i + 1):
            print("*",end="")
        print()

print_diamond(6)

