
f=open("4.txt","r",encoding="utf8")
replace={
    "1":"Одын",
    "2":"Два",
    "3":"Тры",
    "4":"Четыре"
}
f2=open("4_new.txt","w",encoding="utf8")
for s in f:
    sa=s.split()
    f2.write(f"{replace[sa[2]]} - {sa[2]}\n")
f.close()
f2.close()
