"""
Rectangle:

Create a program that prints a rectangle of asterisks with 4 rows and 5 columns:
asciidoc

Copy
***
***
***
***
"""
num_rows = 4
num_cols = 5
for i in range(num_rows):
    for j in range(num_cols):
        print("*" , end="  ")
    print( )
