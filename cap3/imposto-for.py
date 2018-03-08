imposto = ["MEI", "Simples"]
for i in imposto:
    if i.startswith("M"):
        continue
    print(i)