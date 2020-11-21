from functools import reduce

ia=[i for i in range(100,1001) if i%2==0]
print(reduce(lambda a,b:a*b,ia))