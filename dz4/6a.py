from sys import argv
from itertools import count

ca=count(int(argv[1]))
print([next(ca) for x in range(1,100)])
