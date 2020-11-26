
class myException(Exception):
    pass


na = []

while True:
    try:
        a = input("New number :")
        if a == "stop":
            break
        if not a.isdigit():
            raise myException("Not number")
        na.append(int(a))
    except myException as err:
        print(err)

print(na)