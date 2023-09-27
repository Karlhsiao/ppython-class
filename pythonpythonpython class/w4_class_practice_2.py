input_list = input("a1, r, n: ").split()
a1, r, n = [int(x) for x in input_list]
list1 = []
list2 = [a1*r**(i-1) for i in range(1, n+1)]

for i in range(1, n+1):
    list1.append(a1)
    a1 *= r

print(list1)
print(list2)