import json

sp = 0
spi = 0

with open("7.txt","r",encoding="utf8") as f:
    res=[{},{"average":0}]
    for s in f:
        sa=s.split()
        p=float(sa[2])-float(sa[3])
        if p>0:
            sp+=p
            spi+=1
        res[0][sa[0]]=p
if spi>0:
    res[1]['average']=sp/spi
with open("7_out.txt","w",encoding="utf8") as f2:
    f2.write(json.dumps(res))

print("The end")