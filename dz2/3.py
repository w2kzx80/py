m=-100
while m<1 or m>12:
    try:
        m=int(input('vvedite mesiats: '))
    except:
        m=-100
ma=['zima','zima','vesna','vesna','vesna','leto','leto','leto','oseni','oseni','oseni','zima']
print(f"Soglasno listu eto {ma[m-1]}")

ma={
    1: 'zima',
    2: 'zima',
    3: 'vesna',
    4: 'vesna',
    5: 'vesna',
    6: 'leto',
    7: 'leto',
    8: 'leto',
    9: 'oseni',
    10: 'oseni',
    11: 'oseni',
    12: 'zima'
}
print(f"Soglasno slovariu eto {ma.get(m)}")
