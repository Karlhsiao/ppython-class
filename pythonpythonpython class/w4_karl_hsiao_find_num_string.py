a, b, c = [x for x in input("strings: ").split()]

ans = ""

for i in range(0, len(a)):
    if a[i] == b[i] == c[i]:
        ans += a[i]
    else:
        break

print("共同字首為", ans)