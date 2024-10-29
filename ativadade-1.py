# mostrar meu nome
print("-----------------Sistema desenvolvido por Jordão de Sousa Coelho---------------")
print("-------------------------------------------------------------------------------")
# mostrar o menu com os preços das pizzas
print("-----------------------------------| Menu |------------------------------------")
print("-------| Tamanhos |  Pizzas Salgadas (PS) | Pizzas Doces (PD)|-----------------")
print("-------|     P    |      R$ 30.00         |     R$ 34.00     |-----------------")
print("-------|     M    |      R$ 45.00         |     R$ 48.00     |-----------------")
print("-------|     G    |      R$ 60.00         |     R$ 66.00     |-----------------")
print("-------------------------------------------------------------------------------")
print("-------|                APROVEITE NOSSAS PROMOÇÕES           |-----------------")
print("-------------------------------------------------------------------------------")

# iniciar e limpar o acumulador
valorTotal = 0

# limpar a lista de pedidos
pedidos = []

# função para pegar e validar o sabor da pizza
def obter_sabor():
    while True:  # Continua perguntando até ter um valor certo
        sabor = input("\nEscolha o sabor da pizza (PS/PD): ")
        if sabor == "PS" or sabor == "PD":
            return sabor  # Retorna o sabor que foi digitado
        else:
            print("Desculpe, não temos esse sabor. Tente novamente")  # Mostra uma mensagem de erro

# função para pegar e validar o tamanho da pizza
def obter_tamanho():
    while True:  # Continua perguntando até ter um valor certo
        tamanho = input("Escolha o tamanho da pizza (P/M/G): ")
        if tamanho == "P" or tamanho == "M" or tamanho == "G":
            return tamanho  # Retorna o tamanho válido
        else:
            print("Desculpe, não temos esse tamanho. Tente novamente")  # Mostra uma mensagem de erro

# loop para fazer pedidos até o usuário decidir parar
while True:
    # perguntar o sabor da pizza
    sabor = obter_sabor()
    # perguntar o tamanho da pizza
    tamanho = obter_tamanho()

    # determinar o preço com base no sabor e tamanho
    if sabor == "PS":  # esse é pra salgada
        if tamanho == "P":
            preco = 30
        elif tamanho == "M":
            preco = 45
        elif tamanho == "G":
            preco = 60
        saborNome = "salgada"
    elif sabor == "PD":  # esse é pra doce
        if tamanho == "P":
            preco = 34
        elif tamanho == "M":
            preco = 48
        elif tamanho == "G":
            preco = 66
        saborNome = "doce"

    # adicionar o preço ao valor total do pedido
    valorTotal += preco
    # salvar o pedido no array
    pedidos.append(f"Pizza {saborNome} de tamanho {tamanho}, R$ {preco}")

    # mostrar o pedido atual
    print(f"Você pediu uma pizza {saborNome} de tamanho {tamanho}, no valor de R$ {preco}.")

    # perguntar se o usuário deseja fazer mais um pedido
    while True:
        continuar = input("Deseja pedir mais alguma coisa? (sim/não): ")
        if continuar.lower() == "sim":
            break
        elif continuar.lower() == "não":  # se digitar "não", o loop para
            break
        else:
            print("Desculpe, não entendi. Tente novamente.")  # mostrar uma mensagem de erro
            continue

    if continuar.lower() == "não":
        break

# mostrar os pedidos feitos
print("\nPedidos realizados:")
for pedido in pedidos:
    print(pedido)

# mostrar o valor total do pedido
print(f"\nValor total do pedido: R$ {valorTotal}")