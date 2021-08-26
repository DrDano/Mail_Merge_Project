# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: https://www.w3schools.com/python/ref_string_strip.asp

# Use readlines() and for loop to create name variable which will be used to name the files (letters)
# Open the starting_letter.txt file and set mode to "w".
# Use readlines() to create a list called "letter_list"
# Use for loop to pick 0 index of "letter_list" and name it "first_sentence".
# Use first_sentence.replace("[name]", name) to replace "[name]" in letter with Aang.
edited_names_list = []

with open(file="./Input/Names/._invited_names.txt", mode="r") as names_file:
    names_list = names_file.readlines()
    for name in names_list:
        edited_name = name[:-1]
        edited_names_list.append(edited_name)

for name in edited_names_list:
    with open(file=f"./Output/ReadyToSend/{name}.txt", mode="w") as new_letter:
        new_letter.write(f"Dear {name},\n"
                         "You are invited to my birthday this Saturday.\n"
                         "Hope you can make it!\n"
                         "Daniel")
