from erp import (
    cadastrar_cliente,
    cadastrar_produto,
    criar_pedido,
    relatorio_total_por_cliente,
    relatorio_quantidade_por_produto
)

def mostrar_menu():
    print("\n=== MINI ERP (Terminal) ===")
    print("1 - Cadastrar cliente")
    print("2 - Cadastrar produto")
    print("3 - Criar pedido")
    print("4 - Relatório: total por cliente")
    print("5 - Relatório: quantidade por produto")
    print("0 - Sair")

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        cpf = input("CPF do cliente: ").strip()
        nome = input("Nome do cliente: ").strip()
        ok, msg = cadastrar_cliente(cpf, nome)
        print(msg)

    elif opcao == "2":
        codigo = input("Código do produto: ").strip()
        nome = input("Nome do produto: ").strip()
        preco = float(input("Preço (ex: 10.50): ").strip().replace(",", "."))
        estoque = int(input("Estoque: ").strip())
        ok, msg = cadastrar_produto(codigo, nome, preco, estoque)
        print(msg)

    elif opcao == "3":
        cpf = input("CPF do cliente: ").strip()

        itens = []
        while True:
            codigo = input("Código do produto (ENTER para finalizar): ").strip()
            if codigo == "":
                break
            qtd = int(input("Quantidade: ").strip())
            itens.append({"codigo": codigo, "qtd": qtd})

        ok, resp = criar_pedido(cpf, itens)
        if ok:
            print("Pedido criado com sucesso!")
            print(resp)
        else:
            print("Erro:", resp)

    elif opcao == "4":
        print("\nRelatório total por cliente:")
        print(relatorio_total_por_cliente())

    elif opcao == "5":
        print("\nRelatório quantidade por produto:")
        print(relatorio_quantidade_por_produto())

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")