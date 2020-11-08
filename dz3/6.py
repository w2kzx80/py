
def int_func(text):
    return text.capitalize()

sa=input("Vvedite slova: ").split()
for s in sa:
    print(int_func(s),end=" ")
print("")
