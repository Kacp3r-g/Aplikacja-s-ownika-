import random

# Step 1: All possible characters
chars = "*-+/!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# Step 2: Choose password length (you can change the number here)
length = 12  

# Step 3: Generate password
password = ""
for i in range(length):
    password += random.choice(chars)

# Step 4: Print result
print("Twoje hasło to:", password)
