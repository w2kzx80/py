
ta = []
ti = 0
while True:
    ti+=1
    tname = input('Vvedite nazvanie novogo tovara (Enter dlia okonchania spiska): ')
    if tname == "":
        break
    t={"name":tname}
    ta.append((ti,t))
    t["price"] = float(input('Vvedite tzenu: '))
    t["count"] = int(input('Vvedite kolichestvo: '))
    t["ed"] = input('Vvedite edinitsu izmerenia: ')
print(ta)

aa = {"name":[], "price":[], "count":[], "ed":[]}
for ti in ta:
    aa["name"].append(ti[1]["name"])
    aa["price"].append(ti[1]["price"])
    aa["count"].append(ti[1]["count"])
    aa["ed"].append(ti[1]["ed"])

print(f"Analytika: {aa}")
