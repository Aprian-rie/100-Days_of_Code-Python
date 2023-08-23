# Types of Errors

# #File not Found
# with open('a_file.txt') as file:
#     file.read()

# Key Error
# a_dictionary = {"Key": "value}
# value = a_dictionary["non_existent_key"]

# #Index Error
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("Made up Error")


height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human heights should not be over 3 metres")
bmi = weight / height ** 2

print(bmi)
