"""Alphabet Pyramid:

Write a program that prints an alphabet pyramid with 5 rows, where the first row contains A, the second AB, and so on:

Copy
    A
   AB
  ABC
 ABCD
ABCDE"""

def alphabet_pyramid(rows):
    for i in range(rows+1):
        for j in range(i ):
            print(chr(65 + j), end=" ")
        print()
alphabet_pyramid(5)