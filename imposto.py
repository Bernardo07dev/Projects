salario = int(input ("qual seu salário:"))
imposto7 = salario - salario * 0.075
imposto15 = salario - salario * 0.15
imposto22 = salario - salario * 0.225
imposto27 = salario - salario * 0.275

if salario <= 1903:
    print(f"você não pagara nenhum imposto e seu salario será {salario}")
elif salario <= 2826:
    print(f"seu salario final será {imposto7}, e pagara {salario * 0.075} de imposto")
elif salario <= 3751:
    print(f"seu salario final será {imposto15}, e pagara {salario * 0.15} de imposto")
elif salario <= 4664:
    print(f"seu salario final será {imposto22}, e pagara {salario * 0.225} de imposto")
else:
    print(f"seu salario final será {imposto27}, e pagara {salario * 0.275} de imposto")