"""Exercise 9
Write a program that writes the squares of numbers from 1 to 10 into a file ( numbers.txt ), one per
line."""

with open("squares_of_numbers.txt", "w") as f:
    for i in range(1, 11):
        f.write(f"{i**2}\n")