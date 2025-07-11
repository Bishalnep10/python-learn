"""
Simple Pattern:

Use nested loops to print a small pattern of numbers (1 to 2) in a 2x2 format:
basic

Copy
1 1
2 2
"""
num_rows = 2
num_cols = 2
n = 1,2
for i in range(num_rows):
    for j in range(num_cols):
        print(n, end="")
    print()