from data import clientes, produtos, pedidos

def cadastrar_cliente(cpf, nome):
    if cpf in clientes:
        return False, "CPF já cadastrado."
    clientes[cpf] = {"cpf": cpf, "nome": nome}
    return True, "Cliente cadastrado."

def cadastrar_produto(codigo, nome, preco, estoque):
    if codigo in produtos:
        return False, "Produto já cadastrado."
    if preco <= 0:
        return False, "Preço inválido."
    if estoque < 0:
        return False, "Estoque inválido."
    produtos[codigo] = {
        "codigo": codigo,
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }
    return True, "Produto cadastrado."

def criar_pedido(cpf, itens):
    if cpf not in clientes:
        return False, "Cliente não encontrado."

    for item in itens:
        codigo = item["codigo"]
        quantidade = item["qtd"]

        if codigo not in produtos:
            return False, f"Produto {codigo} não existe."
        if quantidade <= 0:
            return False, "Quantidade inválida."
        if produtos[codigo]["estoque"] < quantidade:
            return False, f"Estoque insuficiente para {codigo}."

    total = 0
    for item in itens:
        codigo = item["codigo"]
        quantidade = item["qtd"]
        total += produtos[codigo]["preco"] * quantidade

    desconto = 0
    if total >= 200:
        desconto = total * 0.05

    total_final = total - desconto

    for item in itens:
        codigo = item["codigo"]
        quantidade = item["qtd"]
        produtos[codigo]["estoque"] -= quantidade

    pedido = {
        "cliente": cpf,
        "itens": itens,
        "total": total,
        "desconto": desconto,
        "total_final": total_final
    }

    pedidos.append(pedido)
    return True, pedido

def relatorio_total_por_cliente():
    resumo = {}
    for pedido in pedidos:
        cpf = pedido["cliente"]
        resumo[cpf] = resumo.get(cpf, 0) + pedido["total_final"]
    return resumo

def relatorio_quantidade_por_produto():
    resumo = {}
    for pedido in pedidos:
        for item in pedido["itens"]:
            codigo = item["codigo"]
            quantidade = item["qtd"]
            resumo[codigo] = resumo.get(codigo, 0) + quantidade
    return resumo