"""
Simple Pattern:

Use nested loops to print a small pattern of numbers (1 to 2) in a 2x2 format:
basic

Copy
1 1
2 2
"""
for i in range(2):
    for j in range(2):
        print(i+1,end=" ")
    print()