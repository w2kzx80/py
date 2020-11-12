from sys import argv

print([int(b) for i,b in enumerate(argv[2:]) if int(b)>int(argv[i+1])])