with open("C:/Users/eGovRIDC-Sec/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("C:/Users/eGovRIDC-Sec/Desktop/my_file.txt", mode="a") as file:
    file.write("New text")
