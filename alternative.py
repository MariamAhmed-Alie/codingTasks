string = "That's why her hair is so big. It's full of secrets."

# Create  empty string
alt_char = ""

# Loop through the string alternate uppercase
for i, char in enumerate(string):
    if i % 2 == 0:
        alt_char += char.upper()
    else:
        alt_char += char.lower()

print(alt_char)

#___________________________________________

# Split the string
split_string = string.split()

# Create empty string
alt_word = ""

# Loop through alternate lowercase
for i, word in enumerate(split_string):
    if i % 2 == 0:
        alt_word += word.lower() + " "
    else:
        alt_word += word.upper() + " "

print(alt_word.strip())



 
