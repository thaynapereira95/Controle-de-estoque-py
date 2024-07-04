import json  
import os
from tabulate import tabulate

class Estoque:
    def __init__(self, arquivo='estoque.json'): 
        self.arquivo = arquivo
        self.carregar_estoque() 

    def carregar_estoque(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, 'r') as f:
                self.estoque = json.load(f)
        else:
            self.estoque = {}

    def salvar_estoque(self):
        with open(self.arquivo, 'w') as f:
            json.dump(self.estoque, f, indent=4)

    def adicionar_produto(self, produto, quantidade, valor): 
        if produto in self.estoque:  
            self.estoque[produto]['quantidade'] += quantidade  
        else:
            self.estoque[produto] = {'quantidade': quantidade, 'valor': valor} 
        self.salvar_estoque() 
        print(f"{quantidade} unidades de {produto} adicionadas ao estoque.")
        self.visualizar_estoque()

    def remover_produto(self, produto, quantidade): 
        if produto in self.estoque: 
            if self.estoque[produto]['quantidade'] >= quantidade:
                self.estoque[produto]['quantidade'] -= quantidade  
                if self.estoque[produto]['quantidade'] == 0:
                    del self.estoque[produto] 
                self.salvar_estoque()
                print(f"{quantidade} unidades de {produto} removidas do estoque.")
            else:
                print(f"Quantidade insuficiente de {produto} no estoque.")
        else:
            print(f"{produto} não encontrado no estoque.")
        self.visualizar_estoque()

    def atualizar_produto(self, produto, quantidade, valor):
        if produto in self.estoque:
            self.estoque[produto] = {'quantidade': quantidade, 'valor': valor}
            self.salvar_estoque()
            print(f"{produto} atualizado para {quantidade} unidades e valor {valor}.")
        else:
            print(f"{produto} não encontrado no estoque.")
        self.visualizar_estoque()

    def pesquisar_produto(self, produto): 
        if produto in self.estoque: 
            print(f"{produto}: {self.estoque[produto]['quantidade']} unidades, valor unitário: {self.estoque[produto]['valor']}") 
        else:
            print(f"{produto} não encontrado no estoque.")
        self.visualizar_estoque()

    def visualizar_estoque(self):
        os.system('cls' if os.name == 'nt' else 'clear')  
        if self.estoque:
            print("Estoque atual:")
            tabela = [[produto, info['quantidade'], info['valor']]for produto, info in self.estoque.items()]
            print(tabulate(tabela, headers=["Produto", "Quantidade", "Valor"], tablefmt="pretty"))
        else:
            print("O estoque está vazio.")

def exibir_menu():
    print("====================<<< \033[1;36m MENU \033[m>>>======================")
    print("                                                                       ")
    print("                  Selecione uma opção                                  ")
    print("-------------------------------------------------------                ")
    print("                  CONTROLE DE ESTOQUE                                  ")
    print(" \033[1;36m [1] \033[m Adicionar item                                  ")
    print(" \033[1;36m [2] \033[m Remover item                                    ")
    print(" \033[1;36m [3] \033[m Atualizar item                                  ")
    print(" \033[1;36m [4] \033[m Pesquisar item                                  ")
    print(" \033[1;36m [5] \033[m Visualizar estoque                              ")
    print(" \033[1;36m [6] \033[m Sair                                            ")
    print("======================================================")

def main():
    estoque = Estoque()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            produto = input("Nome do item: ")
            quantidade = int(input("Quantidade: "))
            valor = float(input("Valor unitário: "))
            estoque.adicionar_produto(produto, quantidade, valor)

        elif opcao == "2":
            produto = input("Nome do item: ")
            quantidade = int(input("Quantidade: "))
            estoque.remover_produto(produto, quantidade)

        elif opcao == "3":
            produto = input("Nome do item: ")
            quantidade = int(input("Quantidade: "))
            valor = float(input("Valor unitário: "))
            estoque.atualizar_produto(produto, quantidade, valor)

        elif opcao == "4":
            produto = input("Nome do item: ")
            estoque.pesquisar_produto(produto)

        elif opcao == "5":
            estoque.visualizar_estoque()

        elif opcao == "6":
            print("Saindo...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()


    