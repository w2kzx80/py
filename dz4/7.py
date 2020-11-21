from sys import argv

def fact(n):
    res=1
    for x in range(1,n+1):
        res=res*x
        yield res

for el in fact(int(argv[1])):
    print(el)
