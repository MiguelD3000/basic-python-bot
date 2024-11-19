import json
import os

# Define file path to store user data
user_data_file = 'user_data.json'

# Load user data if it exists
if os.path.exists(user_data_file):
    with open(user_data_file, 'r') as file:
        user_data = json.load(file)
else:
    user_data = {}

# Check if user has been greeted before
name = input("Hello! What is your name? ")
if name in user_data:
    print(f"Welcome back, {name}! Last time you said you are {user_data[name]['age']} years old.")
else:
    print(f"It's a pleasure to meet you, {name}!")
    user_data[name] = {}

while True:
    try:
        age_input = input("Can you please tell me how old you are? (type 'exit' to quit) ")
        if age_input.lower() == 'exit':
            break
        age = int(age_input)
        if age < 0:
            print("Age cannot be negative. Please enter a valid age.")
            continue
        user_data[name]['age'] = age
        bot_age = 7
        if age > bot_age:
            age_difference = age - bot_age
            print(f"Wow, you are {age_difference} years older than me! I'm only {bot_age} years old!")
        elif age < bot_age:
            age_difference = bot_age - age
            print(f"Wow, you are {age_difference} years younger than me! I'm only {bot_age} years old!")
        else:
            print(f"Wow, we are both the same age! I'm also {bot_age} years old!")
        break
    except ValueError:
        print("Oops! That doesn't seem to be a valid number. Could you please enter a valid age?")

if 'age' in user_data[name]:
    color = input("I'd love to know, what's your favorite color? You can enter multiple colors separated by commas. ").strip()
    favorite_colors = [c.strip() for c in color.split(',')] if color else []
    user_data[name]['colors'] = favorite_colors
    if favorite_colors:
        print(f"Oh, {', '.join(favorite_colors)} are indeed beautiful colors!")
    else:
        print("It seems you didn't enter any colors. That's okay!")

# Save user data to file
with open(user_data_file, 'w') as file:
    json.dump(user_data, file, indent=4)

print("Thank you for chatting! Goodbye!")