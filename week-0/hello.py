# This program is a basic hello world app
# created as part of Harvards CS50P

# Ask the user for their name
name = input("What's your name? ").strip().title()

# Split users name into first name and last name
first, last = name.split(" ")

# Say hello to user
print(f"hello, {first}")