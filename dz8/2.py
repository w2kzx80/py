
class myException(Exception):
    pass

try:
    a, b = [int(s) for s in input("Введите a,b (a/b) :").split()]
    if b == 0:
        raise myException("Делить на ноль нельзя")
    print(f"a / b = {a / b}")
except myException as err:
    print(err)
except Exception as err:
        print(err)
