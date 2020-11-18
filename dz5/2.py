
f=open("2.txt","r",encoding="utf8")
scnt=0
for s in f:
    scnt+=1
    print(f"Line {scnt} words count {len(s.split())}")
f.close()
print(f"Total {scnt} lines")