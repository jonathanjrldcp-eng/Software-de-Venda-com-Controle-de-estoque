import os
import time
estoque ={}
lista_venda = []

def limpa_tela():
    input("\nPressione ENTER para limpar a tela...")
    os.system('cls' if os.name == 'nt' else 'clear')

def obter_numero_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print("Por favor, digite um número inteiro positivo.")
                continue
            return valor
        except ValueError:
            print("ERRO: Digite um número inteiro válido.")

def cadastro_produto():
    print("--------CADASTRO DE PRODUTO--------")
    produto = input("DIGITE O NOME DO PRODUTO: ").strip().upper()
    if not produto:
        print("ERRO: insira o nome do produto!!!")
        return
    quantidade = obter_numero_inteiro(f"DIGITE A QUANTIDADE DE '{produto}': ")
    if produto in estoque:
        estoque[produto] += quantidade
        print(f"\nProduto já existia. Estoque atualizado com sucesso!!")
    else:
        estoque[produto] = quantidade
        print(f"\nProduto '{produto}' cadastrado com sucesso!!")

def itens_estoque():
    print("--------ESTOQUE--------")
    if not estoque:
        print("ESTOQUE VAZIO.")
        return
    print(f"{'PRODUTO':<20} | {'QUANTIDADE':>10}")
    print("-"*33)
    for produto, quantidade in estoque.items():
        print(f"{produto:<20} | {quantidade:>10}")

def iniciar_venda():
    print("--------INICIAR VENDA--------")
    if not estoque:
        print("ESTOQUE VAZIO. CADASTRE PRODUTOS ANTES DE INICIAR A VENDA.")
        return
    produto = input("DIGITE O NOME DO PRODUTO PARA VENDA: ").strip().upper()
    if produto not in estoque:
        print(f"ERRO: O produto '{produto}' não foi encontrado no estoque.")
        return
    qtd_disponivel = estoque[produto]
    if qtd_disponivel == 0:
        print(f"O produto '{produto}' não possue unidades (0 unidades)")
        return
    print(f"Quantidade disponível em estoque: {qtd_disponivel}")
    qtd_venda = obter_numero_inteiro("DIGITE A QUANTIDADE QUE DESEJA VENDER: ")
    if qtd_venda == 0:
        print("Venda concelada, produto em falta.")
        return
    if qtd_venda > qtd_disponivel:
        print(f"ERRO: Venda superior {qtd_venda} a quantidade em estoque {qtd_disponivel}")
        return
    estoque[produto] -= qtd_venda
    lista_venda.append({"Produto":produto, "Quantidade":qtd_venda})
    print(f"\nVenda de {qtd_venda} Unidade(s) de '{produto}' completada com sucesso!")

def vendas_vealizadas():
    print("--------VENDAS REALIZADAS--------")
    if not lista_venda:
        print("Nenhuma venda foi realizada")
        return
    total_itens = 0
    print(f"{'PRODUTO':<20} | {'QTD VENDIDA':>12}")
    print("-"*35)
    for venda in lista_venda:
        print(f"{venda['Produto']:<20} | {venda['Quantidade']:>12}")
        total_itens += venda['Quantidade']
    print("*"*35)
    print(f"Total Geral de Produtos Vendidos: {total_itens}")

def main():

    while True:
        print("============== LISTA  ==============")
        print("=============  MENU  ===============")
        print("1 - CADASTRO DE PRODUTO:")
        print("2 - ESTOQUE:")
        print("3 - INICIAR VENDA:")
        print("4 - VENDAS REALIZADAS:")
        print("5 - SAIR:")
        print("===================================")
        opcao = input("DIGITE O NÚMENRO DA OPÇÃO: ").strip()
        limpa_tela()

        if opcao == "1":
            cadastro_produto()
            limpa_tela()

        elif opcao == "2":
            itens_estoque()
            limpa_tela()

        elif opcao == "3":
            iniciar_venda()
            limpa_tela()
        elif opcao == "4":
            vendas_vealizadas()
            limpa_tela()
        elif opcao == "5":
            print("Finalizando o Sistema... Volte sempre!")
            time.sleep(1.5)
            break
        else:
            print("Opção invalida!Opções de 1 a 5.")
            limpa_tela()
if __name__ =="__main__":
    main()