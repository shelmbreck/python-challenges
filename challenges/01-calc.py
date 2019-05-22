# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

calculation = input("What calculation would you like to do? (add, sub, mult, div)?\n")
print(f"{calculation}")
num1 = int(input("What is number 1?\n"))
  print(num1)
num2 = int(input("What is number 2?\n"))
  print(num2)
result = num1 + num2
  print("Your result is", result)
