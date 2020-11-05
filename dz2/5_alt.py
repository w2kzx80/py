
ra = [7, 7, 5, 3, 3, 3, 2 ,2 ]
r = int(input('vvedite znachenie: '))
ri = len(ra)-1
rf = False

if r>ra[0]:
    ra.insert(0,r)
elif r<ra[-1]:
    ra.insert(len(ra),r)
else:
    ri1 = 0
    ri2 = len(ra) - 1
    while ri2-ri1>1:
        rm=(ri1+ri2)//2
        if ra[rm]<r:
            ri2=rm
        else:
            ri1=rm
    if ra[ri2]>=r:
        ra.insert(ri2+1,r)
    elif ra[ri1]>=r:
        ra.insert(ri2,r)
    else:
        ra.insert(ri1,r)
print(ra)
#while not rf:

#while ri>=0:
#    if (ra[ri]>=r):
#        ra.insert(ri+1,r)
#        rf = True
#        break
#    ri-=1
#if not rf:
#    ra.insert(0,r)
#print(ra)
