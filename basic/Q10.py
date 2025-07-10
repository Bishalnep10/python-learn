"""
10.Creating a List from User Input:
Write a program that asks the user to enter 5 names and stores them in a list using a for loop.
"""

a = []

n = 5
for i in range(n):
    element = input(f"Enter names {i+1}: ")
    a.append(element)

print("List:", a)