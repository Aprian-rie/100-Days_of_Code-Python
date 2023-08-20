f1 = open('file1.txt', 'r')
f1_list = f1.readlines()
f1_list_int = [int(n) for n in f1_list]

f2 = open('file2.txt', 'r')
f2_list = f2.readlines()
f2_list_int = [int(n) for n in f2_list]

# print(f1_list_int)
# print(f2_list_int)

result = [num for num in f1_list_int if num in f2_list_int]


# Write your code above 👆

print(result)
