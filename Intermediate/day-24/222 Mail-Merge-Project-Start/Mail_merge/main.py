# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("C:/Users/eGovRIDC-Sec/PycharmProjects/100-Days_of_Code-Python/Intermediate/day-24/222 "
          "Mail-Merge-Project-Start/Mail_merge/Input/Names/invited_names.txt", mode="r") as names:
    name_list = names.readlines()
myname = "Rie"

for name in name_list:
    stripped_name = name.strip()
    with open("C:/Users/eGovRIDC-Sec/PycharmProjects/100-Days_of_Code-Python/Intermediate/day-24/222 "
              "Mail-Merge-Project-Start/Mail_merge/Input/Letters/starting_letter.txt", mode="r") as letter:
        content = letter.read()
        custom_letter = content.replace('[name]', stripped_name)
        ## print(custom_letter)
    with (open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as
          unique_letter):
        unique_letter.write(custom_letter)
