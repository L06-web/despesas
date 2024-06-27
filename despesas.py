import random
from datetime import datetime

def menu():
    print("\n---------- Menu ----------")
    print("1 - Inserir uma despesa: ")
    print("2 - Editar despesa: ")
    print("3 - Buscar despesa: ")
    print("4 - Listar todas as despesas: ")
    print("5 - Remover despesa: ")
    print("6 - Relatório de despesas: ")
    print("7 - Sair: ")
    return input("Escolha uma opção: ")

despesas = []

def inserir():
    def validadata(data_str):
        try:
            datetime.strptime(data_str, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    def validavalor(valor):
        try:
            valor = float(valor)
            if valor > 0:
                return True
            else:
                return False
        except ValueError:
            return False

    id = str(random.randint(0, 99999)).zfill(5)

    data = input("Digite a data da despesa (DD/MM/AAAA): ")
    while not validadata(data):
        print("Data inválida. Por favor, digite novamente.")
        data = input("Digite a data da despesa (DD/MM/AAAA): ")

    categoria = input("Digite a categoria da despesa (ex: alimentação, transporte, lazer, etc.): ")

    descricao = input("Digite a descrição da despesa: ")

    valor = input("Digite o valor da despesa: ")
    while not validavalor(valor):
        print("Valor inválido. Por favor, digite novamente.")
        valor = input("Digite o valor da despesa: ")

    despesa = {
        'id': id,
        'data': data,
        'categoria': categoria,
        'descricao': descricao,
        'valor': float(valor)
    }
    print(despesa)
    despesas.append(despesa)
    print("Despesa adicionada com sucesso!")
    input('Aperte qualquer tecla para continuar')

def editar():
    def validadata(data_str):
        try:
            datetime.strptime(data_str, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    def validavalor(valor):
        try:
            valor = float(valor)
            if valor > 0:
                return True
            else:
                return False
        except ValueError:
            return False

    id = input("Digite o ID da despesa a ser editada: ")
    despesa = next((item for item in despesas if item['id'] == id), None)

    if despesa is None:
        print("Despesa não encontrada.")
        return

    print(f"Editando despesa: {despesa}")

    data = input(f"Digite a nova data da despesa (DD/MM/AAAA) [{despesa['data']}]: ")
    if data:
        while not validadata(data):
            print("Data inválida. Por favor, digite novamente.")
            data = input(f"Digite a nova data da despesa (DD/MM/AAAA) [{despesa['data']}]: ")
        despesa['data'] = data

    categoria = input(f"Digite a nova categoria da despesa [{despesa['categoria']}]: ")
    if categoria:
        despesa['categoria'] = categoria

    descricao = input(f"Digite a nova descrição da despesa [{despesa['descricao']}]: ")
    if descricao:
        despesa['descricao'] = descricao

    valor = input(f"Digite o novo valor da despesa [{despesa['valor']}]: ")
    if valor:
        while not validavalor(valor):
            print("Valor inválido. Por favor, digite novamente.")
            valor = input(f"Digite o novo valor da despesa [{despesa['valor']}]: ")
        despesa['valor'] = float(valor)

    print("Despesa editada com sucesso!")
    input('Aperte qualquer tecla para continuar')

def buscar():
    criterio = input("Informe o critério de busca (data, categoria ou descrição): ").strip().lower()

    if criterio not in ['data', 'categoria', 'descrição']:
        print("Critério inválido.")
        return

    busca = input(f"Digite o termo de busca para {criterio}: ").strip().lower()

    resultados = []
    for despesa in despesas:
        if busca in despesa[criterio].lower():
            resultados.append(despesa)

    if resultados:
        print("Resultados encontrados:")
        for resultado in resultados:
            print(resultado)
    else:
        print("Nenhuma despesa encontrada com os critérios fornecidos.")
    input('Aperte qualquer tecla para continuar')

def listar():
    if not despesas:
        print("Não há despesas cadastradas.")
        return

    print("Listando todas as despesas:\n")
    for despesa in despesas:
        print(f"ID: {despesa['id']}")
        print(f"Data: {despesa['data']}")
        print(f"Categoria: {despesa['categoria']}")
        print(f"Descrição: {despesa['descricao']}")
        print(f"Valor: R$ {despesa['valor']:.2f}\n")
    input('Aperte qualquer tecla para continuar')

def remover():
    id_remover = input("Digite o ID da despesa que deseja remover: ")

    for despesa in despesas:
        if despesa['id'] == id_remover:
            despesas.remove(despesa)
            print(f"Despesa com ID {id_remover} removida com sucesso.")
            return
        else:
            print(f"Despesa com ID {id_remover} não encontrada.")
    input('Aperte qualquer tecla para continuar')

def relatorio():
    if not despesas:
        print("Não há despesas cadastradas para gerar o relatório.")
        return

    relatorio = {}
    total_geral = 0.0

    for despesa in despesas:
        categoria = despesa['categoria']
        valor = despesa['valor']
        if categoria in relatorio:
            relatorio[categoria] += valor
        else:
            relatorio[categoria] = valor
        total_geral += valor

    print("\nRelatório de Despesas:\n")
    for categoria, total_categoria in relatorio.items():
        print(f"Categoria: {categoria} - Total: R$ {total_categoria:.2f}")
    print(f"\nTotal Geral de Despesas: R$ {total_geral:.2f}")
if __name__ == '__main__':
    while True:
        match menu():
            case '1':
                inserir()
            case '2':
                editar()
            case '3':
                buscar()
            case '4':
                listar()
            case '5':
                remover()
            case '6':
                relatorio()
            case '7':
                break
