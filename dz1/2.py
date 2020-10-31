
sec = int(input("Time in seconds: "))
print("Time formatted is: {:02d}:{:02d}:{:02d}".format(sec//3600, (sec%3600)//60, sec%60))
