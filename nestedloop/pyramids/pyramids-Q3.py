"""
Number Pyramid:

Write a program that uses nested loops to print a number pyramid. For example, with 5 rows, the output should be:

Copy
    1
   121
  12321
 1234321
"""


num=int(input("Enter number of rows: "))
for i in range(1,num):
    for j in range(num - i):
        print(" ",end="")
    for k in range(1,i):
        print(k,end="")
    for l in range(i,0,-1):
        print(l,end="")

    print("\n")