# import re
# result = re.match(r'world', 'Hello, world!')
# if result:
#     print("Match found:", result.group())

# import re
# result = re.search(r'world', 'Hello, world!')
# if result:
#     print("Match found:", result.group())

# import re
# text="This is Python Learning, Welcome Folks..."
# # pattern=r"Python"
# pattern=r"This"
# match=re.match(pattern, text)
# if match:
#     print("Match Found", match.group())
# else:
#     print("No Match")
    
# import re
# text="This is Python Learning, Welcome Folks..."
# pattern=r"Welcome"
# search=re.search(pattern, text)
# if search:
#     print("Pattern Found :", search.group())
# else:
#     print("Pattern Not Found")

# import re
# text = "I have 2 apples and 3 bananas."
# new_text = re.sub(r'\d+', 'number', text)
# print(new_text)

# note- in above program, below is expanation -
# {r'\d+': The regular expression pattern \d+ is used to match one or more digits in a row.
# \d matches any digit (0–9).
# + means one or more of the preceding element (in this case, digits).
# 'number': This is the replacement string. Each time a match (a sequence of digits) is found, 
# it will be replaced by the string "number".}


# import re

# text = "The quick brown fox jumps over the lazy brown dog"
# pattern = r"brown"

# replacement = "blue"

# new_text = re.sub(pattern, replacement, text)
# # new_text = re.sub(pattern, "orange", text)
# print("Modified text:", new_text)

# import re

# text = "apple,banana,orange,grape"
# pattern = r","

# split_result = re.split(pattern, text)
# print("Split result:", split_result)

# import re
# text = "The rain in Spain stays mainly in the plain."
# matches = re.findall(r'in', text)
# print(matches) 

# import re

# text = "Contact us at support@example.com or info@example.com"

# # Regex pattern to match email addresses
# pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}'

# emails = re.findall(pattern, text)
# print("The Emails in the text is -", emails)  # ['support@example.com', 'info@company.org']


