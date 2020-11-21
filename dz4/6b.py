from sys import argv
from itertools import cycle

ca=cycle(argv[1:])
print([next(ca) for x in range(1,100)])