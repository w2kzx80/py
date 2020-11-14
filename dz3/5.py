
def process(*args):
    sa=list(args)
    sa+=input("New values? (stopsymbol = S)").split()
    sum = 0
    sf = False
    for s in sa:
        if s=="S":
            sf=True
        elif s.isdigit():
            sum+=int(s)
    print(f"Current sum: {sum}")
    if not sf:
        process(*sa)

process()
