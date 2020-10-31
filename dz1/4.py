
n=-1
while (n<1):
    n=int(input("n int >0: "))

max=0

while (n>0):
    if (n%10 > max):
        max=n%10
    n=n//10
print("Max = {0}".format(max))
