sal = int(input('salario?'))
imp = 27.0
while imp > 0.:
    imp = input("imposto ou (s) para sair")
    if not imp:
        imp = 27.
    elif imp == 's':
        break
    else:
        imp = float(imp)
    print("Valor real: {0}".format(sal - (sal * (imp * 0.01))))
