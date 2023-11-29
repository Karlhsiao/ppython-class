input_list = input().split()

ans = ""

i = 0
min_len = None
count = 0

for word in input_list:
    if min_len == None:
        min_len = len(word)
    min_len = min(len(word), min_len)

for char_index in range(min_len):
    letter_set = set()
    for word in input_list:
        letter_set.add(word[char_index])

    if len(letter_set) == 1:
        count += 1
    
    else:
        break

print("共同字首為", input_list[0][:count])
