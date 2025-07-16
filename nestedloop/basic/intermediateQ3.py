"""Number Pyramid:

Write a program that prints a pyramid of numbers where each row contains increasing numbers:

Copy
  1
 121
12321
1234321"""
num=int(input("Enter a number: "))
for i in range(1,num):
    for j in range(num-i):
        print("",end=" ")
    for k in range(1,i):
        print(k,end="")
    for l in range(i,0,-1):
        print(l,end="")
    print()

print("\n")
