# with open("C:/Users/eGovRIDC-Sec/Desktop/my_file.txt") as file:
#     contents = file.read()
#     print(type(contents))
#
# with open("C:/Users/eGovRIDC-Sec/Desktop/my_file.txt", mode="a") as file:
#     file.write("New text")
#
# file_list = []
#
# with open("C:/Users/eGovRIDC-Sec/Desktop/my_file.txt", mode="a") as file:
#     file_list.append(file.write("New text"))
# #
# for i in file_list:
#     print(file_list[i - 1])
#
for i in range(3):
    with open('data.txt', 'r') as fp1, open(f"C:/Users/eGovRIDC-Sec/Desktop/text{i}.txt", 'w') as fp2:
        results = fp1.read()
        fp2.write(results)
