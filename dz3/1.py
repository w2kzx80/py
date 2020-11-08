
def div(a,b):
    try:
        return a/b
    except Exception as e:
        print(f"Error: {e}")

a, b = input("Insert a, b [using space as delimiter]: ").split()
a=float(a)
b=float(b)
print(div(a,b))
