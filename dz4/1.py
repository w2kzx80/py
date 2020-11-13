from sys import argv

def zp(hrs,ph,pr):
    return hrs*ph+pr

print(zp(int(argv[1]),int(argv[2]),int(argv[3])))
