
firm_plus=float(input("Finance +: "))
firm_minus=float(input("Finance -: "))

rent=0.0

if (firm_plus>firm_minus):
    print("Pribili!!")
    print("Rentabilinosti = {0}".format((firm_plus-firm_minus)/firm_plus))
    workers = int(input("Skoliko rabotnikov?: "))
    print("Pribili/sotrudnika: {0}".format((firm_plus-firm_minus)/workers))
else:
    print("(((")

