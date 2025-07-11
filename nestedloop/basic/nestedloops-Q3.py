"""
Right-Angled Triangle:

Use nested loops to print a right-angled triangle of asterisks with 4 rows:

Copy
*
**
***
"""
num_rows = 4
for row in range(1,num_rows+1):
    for column in range(1,row+1):
        print("*",end=" ")
    print()