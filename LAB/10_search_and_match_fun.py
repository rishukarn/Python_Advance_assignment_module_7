#  Write a Python program to search for a word in a string using re.search().
#  Write a Python program to match a word in a string using re.match().

import re

# Input string
text = "Python is a powerful programming language."

# Search for the word "powerful"
match = re.search(r"\bpowerful\b", text)

if match:
    print("Word found:", match.group())
else:
    print("Word not found.")
    

match = re.match(r"Python", text)

if match:
    print("Matched:", match.group())
else:
    print("No match found.")