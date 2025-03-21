entrar = input("você quer entrar na calculadora")

if entrar == "sim":
    numero1 = float(input("Me de o primeiro número"))
    numero2 = float(input("Me de o segundo número"))
    operação = input("qual operação você quer fazer")
    if operação == "vezes":
        print(f"{numero1} vezes {numero2} é igual a {numero1 * numero2}")
    elif operação == "soma":
        print(f"{numero1} mais {numero2} é igual a {numero1 + numero2}")
    elif operação == "subtração":
        print(f"{numero1} menos {numero2} é igual a {numero1 - numero2}")
    elif operação == "divisão":
        print(f"{numero1} dividido {numero2} é igual a {numero1 / numero2}")
else:
    print("A calculadora será desativada")