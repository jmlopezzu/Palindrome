# Palindrome checker

# For character strings

string = '''ojó'''

### Convert to lowercase

lowercase = string.lower()
words = lowercase.split()

print(words)

# Remove punctuation

plane_list = []

for w in words:
  q = w.strip(".").strip(",")
  plane_list.append(q)

print(plane_list)

plane_string = " ".join(plane_list)

print(plane_string)

# Omit accent marks

plane_string = plane_string.replace("á", "a").replace("é", "e")\
  .replace("í", "i").replace("ó", "o").replace("ú", "u")

print(plane_string)

# Reverse string

reverse_string = plane_string[::-1]

print(reverse_string)

# Compare strings

if plane_string == reverse_string:
  print("Palindrome")
else:
  print("Not a palindrome")






