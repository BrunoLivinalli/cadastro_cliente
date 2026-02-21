import csv
import re
import os

# Nome do arquivo onde os dados serão salvos
ARQUIVO = "clientes.csv"

# FUNÇÕES DE VALIDAÇÃO
def validar_cpf(cpf):
    """
    Remove pontos e traços e verifica se tem apenas números e
    se tem exatamente 11 dígitos
    """
    cpf = cpf.replace(".", "").replace("-", "")
    return cpf.isdigit() and len(cpf) == 11


def validar_email(email):
    """
    Usa uma expressão regular (regex) simples
    para checar se o email está no formato correto.
    """
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email) is not None


def validar_telefone(telefone):
    """
    Remove caracteres especiais e valida se possui apenas números
    e tem entre 9 e 11 dígitos 
    """
    telefone = telefone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
    return telefone.isdigit() and 9 <= len(telefone) <= 11


# FUNÇÕES DE ARQUIVO CSV
def carregar_dados():
    """
    Lê o arquivo CSV e retorna uma lista de dicionários.
    Caso o arquivo não exista ainda, retorna lista vazia.
    """
    if not os.path.exists(ARQUIVO):
        return []

    with open(ARQUIVO, "r", newline="", encoding="utf-8") as csvfile:
        leitor = csv.DictReader(csvfile)
        return list(leitor)


def salvar_dados(clientes):
    """
    Recebe uma lista de clientes (dicionários)
    e escreve tudo no arquivo CSV.
    """
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as csvfile:
        campos = ["nome", "cpf", "email", "telefone"]
        escritor = csv.DictWriter(csvfile, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(clientes)



# FUNÇÕES PRINCIPAIS DO SISTEMA
def cadastrar_cliente(clientes):
    """
    Coleta dados do usuário, faz validações
    e adiciona no sistema + CSV.
    """
    nome = input("Nome: ").strip()

    # Valida CPF
    cpf = input("CPF (apenas números): ").strip()
    while not validar_cpf(cpf):
        print("CPF inválido! Deve conter 11 dígitos numéricos.")
        cpf = input("Digite novamente o CPF: ")

    # Valida Email
    email = input("E-mail: ").strip()
    while not validar_email(email):
        print("E-mail inválido!")
        email = input("Digite novamente o e-mail: ")

    # Valida Telefone
    telefone = input("Telefone (com DDD): ").strip()
    while not validar_telefone(telefone):
        print("Telefone inválido!")
        telefone = input("Digite novamente o telefone: ")

    # Cria o dicionário representando o cliente
    cliente = {
        "nome": nome,
        "cpf": cpf,
        "email": email,
        "telefone": telefone
    }

    # Adiciona à lista
    clientes.append(cliente)

    # Salva no CSV
    salvar_dados(clientes)

    print("\nCliente cadastrado com sucesso!\n")


def listar_clientes(clientes):
    """
    Mostra todos os clientes cadastrados no CSV.
    """
    if len(clientes) == 0:
        print("\nNenhum cliente cadastrado.\n")
        return

    print("\n=== CLIENTES CADASTRADOS ===")
    for i, cliente in enumerate(clientes, 1):
        print(
            f"{i}. Nome: {cliente['nome']} | CPF: {cliente['cpf']} | "
            f"E-mail: {cliente['email']} | Telefone: {cliente['telefone']}"
        )
    print()



# MENU PRINCIPAL
def menu():
    """
    Controla o fluxo do programa.
    """
    clientes = carregar_dados()

    while True:
        print("SISTEMA DE CADASTRO DE CLIENTES ")
        print("1- Cadastrar cliente")
        print("2- Listar clientes")
        print("3- Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente(clientes)

        elif opcao == "2":
            listar_clientes(clientes)

        elif opcao == "3":
            print("Encerrando.")
            break

        else:
            print("Opção inválida!\n")


# Inicia o programa
menu()