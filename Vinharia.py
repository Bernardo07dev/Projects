print("Olá, boas-vindas a Vinharia Agnello")

endereço = input("Qual o seu endereço?")
nascimento = int(input("Qual sua ano de nascimento?"))
idade = 2025 - nascimento

if idade >= 18:
    print("Ótimo, vamos prosseguir")
    print("Temos 3 opções de vinho, são elas 'tinto - R$90', 'branco - R$120'' e ''rose - R$140'")
    tipo = input("Qual opção de vinho você irá querer?")
    if tipo == "tinto":
            valor = 90
    elif tipo == "branco":
            valor = 120
    elif tipo == "rose":
            valor = 140
    garrafas = int(input(f"Quantos garrafas de vinho {tipo}?"))
    final = valor * garrafas
    if final > 100:
        frete = 0
    else:
        frete = 10
    print(f"Perfeito, valor de {garrafas} garrafa(s) de vinho {tipo} será {final} e seu frete será de {frete}")
    print(f"Obrigado por comprar na vinharia agnello, o preço de {garrafas} vinho(s) será de {final + frete} e iremos entregar na sua casa, no endereço {endereço}")

else:
    print(f"Não será possível fazer a compra e a venda não é permitida, você é menor de idade e ainda tem R${idade},00")