f =open('file.txt', 'r')
list = f.readlines()
print(list)

new_list = [int(n) for n in list]

print((new_list))