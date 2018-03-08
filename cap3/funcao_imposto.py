def salario_desconto_imposto(salario, imposto = 27.0):
    return salario - (salario * imposto * 0.01)

print(salario_desconto_imposto(5000))
