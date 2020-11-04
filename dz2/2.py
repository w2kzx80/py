
s = input("Vvedite cherez probely spisok: ").split()
l2 = len(s) // 2
while l2>0:
    s[l2*2-1], s[l2*2-2] = s[l2*2-2], s[l2*2-1]
    l2-=1
print(s)