def getInts(s):
    i1=-1
    i2=-1
    for i in range(0,len(s)):
        if s[i] in '0123456789':
            if i1==-1:
                i1=i
                i2=i
            else:
                i2=i
        else:
            if i1!=-1:
                yield(int(s[i1:i2+1]))
            i1=-1
            i2=-1
    if i1!=-1:
        yield(int(s[i1:i2 + 1]))

f=open("6.txt","r",encoding="utf8")
lessons={}
for s in f:
    lessons[s.split(':')[0]]=sum([int(x) for x in getInts(s)])
f.close()
print(lessons)