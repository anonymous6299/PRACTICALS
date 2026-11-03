import re

# Sample text
text = """
Name: Rahul
Email: rahul@gmail.com
Phone: 9876543210
Website: www.example.com
"""

# 1. Search for a word
result = re.search(r'Rahul', text)
print("Search Result:", result.group() if result else "Not Found")

# 2. Find all numbers
numbers = re.findall(r'\d+', text)
print("\nNumbers Found:", numbers)

# 3. Extract email address
email = re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)
print("\nEmail Address:", email)

# 4. Extract phone number
phone = re.findall(r'\b\d{10}\b', text)
print("\nPhone Number:", phone)

# 5. Replace a word
new_text = re.sub(r'Rahul', 'Amit', text)
print("\nModified Text:")
print(new_text)

# 6. Validate email address
test_email = "student@gmail.com"

if re.fullmatch(r'[\w.-]+@[\w.-]+\.\w+', test_email):
    print("Valid Email Address")
else:
    print("Invalid Email Address")

# 7. Split text using whitespace
words = re.split(r'\s+', "Python is easy to learn")
print("\nSplit Words:", words)