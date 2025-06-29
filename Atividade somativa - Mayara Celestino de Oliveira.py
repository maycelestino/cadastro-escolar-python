# Mayara Celestino de Oliveira - Análise e desenvolvimento de Sistemas

# Lista/dicionário para mapear as opções numéricas aos nomes
opcao_menu = {
    '1': "[Estudantes]",
    '2': "[Disciplinas]",
    '3': "[Professores]",
    '4': "[Turmas]",
    '5': '[Matrículas]',
    '9': "[Sair]"
}

# Listas para armazenar os dados
lista_estudantes = []
lista_professores = []
lista_disciplinas = []
lista_turmas = []
lista_matriculas = []

def listar_dados(lista, tipo):
    if lista:
        print(f"\nLista de {tipo}:\n")
        for item in lista:
            print(f"- {item}")
    else:
        print(f"\nNão há {tipo} cadastrados.\n")

def incluir_item(lista, item):
    lista.append(item)
    print(f"\n{item} foi incluído com sucesso.\n")

def atualizar_item(lista, codigo, novos_dados):
    for item in lista:
        if item["Código"] == codigo:
            item.update(novos_dados)
            print(f"{novos_dados["Nome"]} atualizado com sucesso.")
            return
    print("Código não encontrado.")

def excluir_item(lista, codigo):
    for i, item in enumerate(lista):
        if item["Código"] == codigo:
            del lista[i]
            print(f"{item["Nome"]} excluído com sucesso.")
            return
    print("Código não encontrado.")

def validar_codigo(lista, codigo):
    return any(item["Código"] == codigo for item in lista)

# Apresentando ao usuário o Menu principal
while True:  # Loop para manter o menu principal ativo até o usuário selecionar "Sair"

    print(" ------ MENU PRINCIPAL ------ \n")
    print("1. Estudantes")
    print("2. Disciplinas")
    print("3. Professores")
    print("4. Turmas")
    print("5. Matrículas")
    print("9. Sair \n")

    # Solicitando ao usuário que selecione uma opção
    opcao = input("Selecione uma opção: ")

    # Realizando a leitura do usuário
    if opcao == "1":
        print("\nVocê entrou no menu de Estudantes.\n")
    elif opcao == "2":
        print("\nVocê entrou no menu de Disciplinas.\n")
    elif opcao == "3":
        print("\nVocê entrou no menu de Professores.\n")
    elif opcao == "4":
        print("\nVocê entrou no menu de Turmas.\n")
    elif opcao == "5":
        print("\nVocê entrou no menu de Matrículas.\n")
    elif opcao == "9":
        print("\nVocê saiu do sistema.\n")
        break  # Encerra o loop e o sistema
    else:
        print("\nOperação inválida\n")
        continue  # Volta ao início do loop principal se a opção for inválida

    # Segundo loop do sistema para o menu de operações
    while True:
        # Criando o menu de navegações
        print(f"\n----- {opcao_menu[opcao].upper()} MENU DE OPERAÇÕES  -----\n")
        print("1. Incluir")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Excluir")
        print("5. Voltar ao menu Principal")

        # Solicitando uma opção ao usuário
        opcao2 = input("\nSelecione uma opção: ")

        # Realizando a leitura de escolha do usuário
        if opcao2 == "1":
            if opcao == "1":  # Estudantes
                nome_estudante = input("Digite o nome do estudante: ")
                codigo_estudante = len(lista_estudantes) + 1  # Atribuindo código único
                incluir_item(lista_estudantes, {"Código": codigo_estudante, "Nome": nome_estudante})
            elif opcao == "2":  # Disciplinas
                codigo_disciplina = int(input("Digite o código da disciplina: "))
                nome_disciplina = input("Digite o nome da disciplina: ")
                if not validar_codigo(lista_disciplinas, codigo_disciplina):
                    incluir_item(lista_disciplinas, {"Código": codigo_disciplina, "Nome": nome_disciplina})
                else:
                    print("Código da disciplina já existe.")
            elif opcao == "3":  # Professores
                codigo_professor = int(input("Digite o código do professor: "))
                nome_professor = input("Digite o nome do professor: ")
                cpf_professor = input("Digite o CPF do professor: ")
                if not validar_codigo(lista_professores, codigo_professor):
                    incluir_item(lista_professores, {"Código": codigo_professor, "Nome": nome_professor, "CPF": cpf_professor})
                else:
                    print("Código do professor já existe.")
            elif opcao == "4":  # Turmas
                codigo_turma = int(input("Digite o código da turma: "))
                codigo_professor = int(input("Digite o código do professor: "))
                codigo_disciplina = int(input("Digite o código da disciplina: "))
                if not validar_codigo(lista_turmas, codigo_turma):
                    incluir_item(lista_turmas, {"Código": codigo_turma, "Código do professor": codigo_professor, "Código da disciplina": codigo_disciplina})
                else:
                    print("Código da turma já existe.")
            elif opcao == "5":  # Matrículas
                codigo_turma = int(input("Digite o código da turma: "))
                codigo_estudante = int(input("Digite o código do estudante: "))
                incluir_item(lista_matriculas, {"Código da turma": codigo_turma, "Código do estudante": codigo_estudante})
        elif opcao2 == "2":
            if opcao == "1":
                listar_dados(lista_estudantes, "Estudantes")
            elif opcao == "2":
                listar_dados(lista_disciplinas, "Disciplinas")
            elif opcao == "3":
                listar_dados(lista_professores, "Professores")
            elif opcao == "4":
                listar_dados(lista_turmas, "Turmas")
            elif opcao == "5":
                listar_dados(lista_matriculas, "Matrículas")
        elif opcao2 == "3":
            if opcao == "1":  # Atualizar Estudantes
                codigo_estudante = int(input("Digite o código do estudante que deseja atualizar: "))
                novo_nome = input("Digite o novo nome do estudante: ")
                atualizar_item(lista_estudantes, codigo_estudante, {"Nome": novo_nome})
            elif opcao == "2":  # Atualizar Disciplinas
                codigo_disciplina = int(input("Digite o código da disciplina que deseja atualizar: "))
                novo_nome = input("Digite o novo nome da disciplina: ")
                atualizar_item(lista_disciplinas, codigo_disciplina, {"Nome": novo_nome})
            elif opcao == "3":  # Atualizar Professores
                codigo_professor = int(input("Digite o código do professor que deseja atualizar: "))
                novo_nome = input("Digite o novo nome do professor: ")
                novo_cpf = input("Digite o novo CPF do professor: ")
                atualizar_item(lista_professores, codigo_professor, {"Nome": novo_nome, "CPF": novo_cpf})
            elif opcao == "4":  # Atualizar Turmas
                codigo_turma = int(input("Digite o código da turma que deseja atualizar: "))
                novo_codigo_professor = int(input("Digite o novo código do professor: "))
                novo_codigo_disciplina = int(input("Digite o novo código da disciplina: "))
                atualizar_item(lista_turmas, codigo_turma, {"Código do professor": novo_codigo_professor, "Código da disciplina": novo_codigo_disciplina})
            elif opcao == "5":  # Atualizar Matrículas
                codigo_matricula = int(input("Digite o código da matrícula que deseja atualizar: "))
                novo_codigo_turma = int(input("Digite o novo código da turma: "))
                novo_codigo_estudante = int(input("Digite o novo código do estudante: "))
                atualizar_item(lista_matriculas, codigo_matricula, {"Código da turma": novo_codigo_turma, "Código do estudante": novo_codigo_estudante})
        elif opcao2 == "4":
            if opcao == "1":  # Excluir Estudantes
                codigo_estudante = int(input("Digite o código do estudante que deseja excluir: "))
                excluir_item(lista_estudantes, codigo_estudante)
            elif opcao == "2":  # Excluir Disciplinas
                codigo_disciplina = int(input("Digite o código da disciplina que deseja excluir: "))
                excluir_item(lista_disciplinas, codigo_disciplina)
            elif opcao == "3":  # Excluir Professores
                codigo_professor = int(input("Digite o código do professor que deseja excluir: "))
                excluir_item(lista_professores, codigo_professor)
            elif opcao == "4":  # Excluir Turmas
                codigo_turma = int(input("Digite o código da turma que deseja excluir: "))
                excluir_item(lista_turmas, codigo_turma)
            elif opcao == "5":  # Excluir Matrículas
                codigo_matricula = int(input("Digite o código da matrícula que deseja excluir: "))
                excluir_item(lista_matriculas, codigo_matricula)
        elif opcao2 == "5":
            print("\nVoltando ao menu principal...\n")
            break  # Sai do loop de operações e retorna ao menu principal
        else:
            print("\nOperação inválida\n")

print('Finalizando aplicação...')
