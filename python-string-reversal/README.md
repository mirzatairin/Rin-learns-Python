# String Reversal and Palindrome Check in Python

This is a comprehensive documentation on how we use **Python slicing** to reverse a string and check whether a string is a palindrome.

---

# Code Overview

```python
def reverse_text(text):
    return text[::-1]


string = "Rin was here"

new_string = reverse_text(string)

print(new_string)
```

---

# Function Explanation

- `def` means "define a function"
- `reverse_text` is the name of the function
- `text` is the parameter (input)

This function reverses a string using Python's slicing syntax.

---

# How Slicing Works

Example:

```python
text = "abcdefg"

print(text[1:5:2])
```

---

# Index Breakdown

```text
a b c d e f g
0 1 2 3 4 5 6
```

- Index `1` = `b`
- Index `5` = `f`

---
# Step-by-Step Execution

- Start at index `1` → `b`
- Move forward by `2` → index `3` → `d`
- Move forward by `2` again → reaches index `5`
- Index `5` is the stop index, so it is excluded

---
# Final Output

```text
bd
```

# Slice Format

The general slicing syntax is:

```text
[start:stop:step]
```

Meaning:

- Start at index `1`
- Stop before index `5`
- Step size = `2`

---

# Important Concept

This does NOT mean simply selecting indexes `1` and `4`.

Instead, it means:

> Start at the beginning point and move forward according to the step value until the stop boundary is reached.

---

---

# Palindrome Concept

A palindrome is a string that reads the same forward and backward.

Examples:

- AHA
- madam
- level

---

# Palindrome Checker Code

```python
def reverse_text(text):
    return text[::-1]


user_input = input("Enter some text: ")

new_string = reverse_text(user_input)

if user_input == new_string:
    print("String is a palindrome")
else:
    print("String is not a palindrome")
```

---

# Example Run

```text
Enter some text: madam
String is a palindrome
```

---

# Key Takeaways

- `[::-1]` is a Pythonic way to reverse a string
- `[start:stop:step]` provides control over slicing behavior
- Step size determines how indexes are skipped
- Palindromes are identified by comparing the original string with its reversed version
- Functions allow reusable and organized code

---

# Author

Rin
