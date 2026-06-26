tarefas = []

def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {
        "nome": nome_tarefa,
        "concluida": False
        }
    tarefas.append(tarefa)
    print(f"Tarefa '{nome_tarefa}' adicionada com sucesso!")
    return

def ver_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return

    print("Tarefas:")
    for i, tarefa in enumerate(tarefas):
        status = "✔" if tarefa["concluida"] else " "
        print(f"{i + 1}. [{status}] {tarefa['nome']}")

def atualizar(tarefas):
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return

    ver_tarefas(tarefas)
    indice = int(input("Digite o número da tarefa que deseja atualizar: ")) - 1

    if 0 <= indice < len(tarefas):
        nova_tarefa = input("Digite o novo nome da tarefa: ")
        tarefas[indice]["nome"] = nova_tarefa
        print("Tarefa atualizada com sucesso!")
    else:
        print("Índice inválido.")

def deletar(tarefas):
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return

    for tarefa in tarefas:
        if tarefa["concluida"]:
            tarefas.remove(tarefa)
    print("Tarefas concluídas deletadas com sucesso!")

while True:
    print("Gerenciador de Tarefas")
    print("1. adicinar tarefa")
    print("2. listar tarefas")
    print("3. marcar tarefa como concluída")
    print("4. atualizar tarefa")
    print("5. deletar tarefas completadas")
    print("6. sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome_tarefa = input("qual o nome da sua tarefa? ")
        if nome_tarefa != "":
            adicionar_tarefa(tarefas, nome_tarefa)
        else:
            print("O nome da tarefa não pode ser vazio.")
    elif escolha == "2":
        print("Lista de tarefas:")
        ver_tarefas(tarefas)
    elif escolha == "3":
        ver_tarefas(tarefas)
        indice = int(input("Digite o número da tarefa que deseja marcar como concluída: ")) - 1

        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = True
            print("Tarefa marcada como concluída!")
        else:
            print("Índice inválido.")
    elif escolha == "4":
        atualizar(tarefas)
    elif escolha == "5":
        deletar(tarefas)
        ver_tarefas(tarefas)
    elif escolha == "6":
        print("Saindo do gerenciador de tarefas...")
        break
