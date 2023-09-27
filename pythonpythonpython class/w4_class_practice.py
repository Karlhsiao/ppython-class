a = int(input("a="))
d = int(input("d="))
n = int(input("n="))

ans = []

for i in range(1, n+1):
    ans.append(a)
    a += d 
    
print(ans)

