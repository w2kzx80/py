
f=open("1.txt","w",encoding="utf8")
s=input()
while s!="":
    f.write(f"{s}\n")
    s=input()
f.close()
