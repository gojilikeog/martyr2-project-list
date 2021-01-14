# Check if Palindrome

example = input("Give me a phrase: ")

if example == example[::-1]:
    print("This phrase is a palindrome!")
else:
    print("Just a regular phrase.")
