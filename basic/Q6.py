"""
5. Nested Loops:
Create a multiplication table (from 1 to 5) using nested for loops.
"""
for i in range(1, 6):
    print(f"Multiplication Table for {i}:")
    for j in range(1, 6):
        product = i * j
        print(f"{i} x {j} = {product}")
    print()
