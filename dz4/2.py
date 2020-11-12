from sys import argv

def gcheck(a):
    prev = int(a[0])
    for acur in a:
        if int(acur)>prev:
            yield int(acur)
            prev=int(acur)

print([a for a in gcheck(argv[1:])])