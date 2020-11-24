import random
rs=0
f=open("5.txt","w",encoding="utf8")
for i in range(0,15):
    r=random.randint(1,1000)
    f.write(f"{r} ")
    rs+=r
print(f"Sum = {rs}")
f.close()