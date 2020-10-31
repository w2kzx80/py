
print("Hi, bro) Lets check Your alcohol state..")
alco = ""
while alco not in {"whiskey","wine","beer"}:
    alco = input("Well.. first of all - which alcohol did You drink? whiskey / wine / beer / none ?")

alco_coef = 0.0
if (alco == "none"):
    print("You are joking)")
    quit()
elif (alco == "wine"):
    print("You are gentlemen!")
    alco_coef = 0.12
elif (alco == "beer"):
    print("\U0001F91F")
    alco_coef=0.05
else:
    print("Whiskey!!")
    alco_coef=0.4

gm = input("well.. how many gramm You drunk?")
gm = int(gm)

print("So now Your alcohol is..%s gm " % (gm*alco_coef*0.8))
kg = int(input("Which is Your weight in kg?"))

print("Lets calc...")
c=((gm*alco_coef*0.8)/(kg*0.65))
print("Your concentration of alc is ~ %s ‰" % c)
print("You will be ok after %s hrs " % (c/0.15))

