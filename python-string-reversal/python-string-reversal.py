# Function to reverse a string
def reverse_text(text):
    return text[::-1]


# Example using a predefined string
string = "Rin is learning Python!"

# Call the function and store the reversed result
new_string = reverse_text(string)

# Print the reversed string
print("Reversed text:", new_string)


# -----------------------------------------
# Taking input from the user
# -----------------------------------------

# Ask the user to enter some text
user_input = input("Enter some text: ")

# Reverse the user's input
new_string = reverse_text(user_input)

# Print the reversed version
print("Reversed text:", new_string)


# -----------------------------------------
# Palindrome Check
# -----------------------------------------

# Compare the original text with the reversed text
if user_input == new_string:
    print("String is a palindrome")
else:
    print("String is not a palindrome")