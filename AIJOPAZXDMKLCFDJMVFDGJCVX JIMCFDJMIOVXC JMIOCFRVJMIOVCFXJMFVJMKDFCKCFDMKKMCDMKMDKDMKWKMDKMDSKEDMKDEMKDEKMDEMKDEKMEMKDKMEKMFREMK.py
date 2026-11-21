p = input("What's your name?: ")
p1 = p
print(f"Hello, {p1}.")
print("My name is guy.")
print("I like some things.")
try:
   g = int(input("Enter a first number for addition: "))
   g1 = int(input("Enter the second number: "))
   print(f"{g} + {g1} is {g + g1}.")
except ValueError:
   print("Brother, don't u know what a number means?")