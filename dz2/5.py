
ra = [7, 5, 3, 3, 2]
r = int(input('vvedite znachenie: '))
ri = len(ra)-1
rf = False
while ri>=0:
    if (ra[ri]>=r):
        ra.insert(ri+1,r)
        rf = True
        break
    ri-=1
if not rf:
    ra.insert(0,r)
print(ra)
