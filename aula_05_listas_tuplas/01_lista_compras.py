# Aula 05 - Lista de Compras Dinâmica

compras = [] # Lista vazia

while True:
    print("\n1. Adicionar item | 2. Ver lista | 3. Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        item = input("O que comprar? ")
        compras.append(item) # Adiciona no final
        print(f"'{item}' adicionado!")
    elif opcao == "2":
        print("Sua lista:", compras)
    elif opcao == "3":
        print("Fechando lista...")
        break # Sai do loop
    else:
        print("Opção inválida!")