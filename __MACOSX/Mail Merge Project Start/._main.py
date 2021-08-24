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

with open(file="../Names/._invited_names.txt", mode="r") as names_file:
    names_list = names_file.readlines()

for name in names_list:
    with open(file=f"./ReadyToSend/name{name}", mode="w") as


