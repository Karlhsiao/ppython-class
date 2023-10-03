str_list = input("input: ").split()

count = 0

for i in str_list:
    if i[0] == i[-1]:
        count += 1

print("output:", count)