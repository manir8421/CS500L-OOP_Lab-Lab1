# Python Lab (CS500L)/Week:01/Lab:01/Q:02
# 20099_MANIRUZZAMAN_MD
# Program for a string as input and returns a version with each word capitalized and a full stop added at the end.

m = input("Enter the input string: ")          # For taking input from keyboard

z = ""                                         # empty string called for store final result
x = True                                       # boolean function use to track next character checking in a loop

for character in m:                            # start the loop
    if character.isalpha():                    # Check the character is an alphabet letter
        if x:
            z += character.capitalize()        # Capitalize the first letter of each word
            x = False
        else:
            z += character.lower()             # Lowercase the rest of the letters
    elif character.isspace():                  # check the current character is space
        x = True
        z += character                         # Add space in the result
    else:
        z += character                         # add current (non alphabet) character

full_stop = (".")                              # Using full stop (.) as a string
y = z + full_stop

print("Output is:", y)                         # Output print