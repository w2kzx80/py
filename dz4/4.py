from sys import argv

print([int(i) for i in argv[1:] if argv[1:].count(i)==1])