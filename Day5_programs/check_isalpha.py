#Take name as an input from the user and check whether it contains alphabet or not


def alphabet(name):
  if name.isalpha():
    print(f"Hello, {name}! How are you today")
  else:
    print("Please enter a valid name with alphabetic characters only")

name=input("Enter your friend's name: ")
alphabet(name)