while True:
    print("Gerenciador de Tarefas")
    print("1. adicinar tarefa")
    print("2. listar tarefas")
    print("3. marcar tarefa como concluída")
    print("4. atualizar tarefa")
    print("5. deletar tarefas completadas")
    print("6. sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "6":
        print("Saindo do gerenciador de tarefas...")
        break
