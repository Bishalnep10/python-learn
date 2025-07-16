"""Hollow Square:

Write a program that prints a hollow square of asterisks with a size of 5:
asciidoc

Copy
***
*   *
*   *
*   *
***"""
size = 5
print("*" * size)
for i in range(size - 2):
    print("*" + " " * (size - 2) + "*")
if size>1:
            print("*" * size)