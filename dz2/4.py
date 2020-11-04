
sa=input('vvedite slova: ').split()
si = 0
for s in sa:
    si+=1
    print(f"{si}: {s[:10:1]}")
