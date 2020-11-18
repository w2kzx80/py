
f=open("3.txt","r",encoding="utf8")
mzp=0
mcnt=0
for s in f:
    zp=int(s.split()[1])
    if zp<20000:
        print(s.split()[0])
    mzp+=zp
    mcnt+=1
f.close()
if mcnt==0:
    print("No data")
else:
    print(f"Average {mzp/mcnt}")