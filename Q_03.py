
# Python Lab (CS500L)/Week:01/Lab:01/Q:03
# 20099_MANIRUZZAMAN_MD
# Write a function that takes a string as input and returns True if it's a palindrome, False otherwise.

print("Checking here, if a string is a palindrome")

#get the input string from the user

text = input("Enter a string: ")

left_index = 0
right_index = len(text) - 1

is_palindrome = True

while left_index < right_index:
    if text[left_index] != text[right_index]:
        is_palindrome = False
        break
    left_index += 1
    right_index -= 1

#  print the result
if is_palindrome is True:
    print("The string", text, "is a palindrome")
else:
    print("The string", text, "is not a palindrome")
    


