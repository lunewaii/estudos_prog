# o contato vai ter nome, telefone, email e se é favorito ou não
contato = []

def adicionar(nome, telefone, email):
    dados = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": False
    }
    contato.append(dados)
    print(f"Contato '{nome}' adicionado com sucesso!")

def listar():
    if contato == []:
        print("Nenhum contato encontrado.")
        return

    print("Contatos:")
    for i, c in enumerate(contato):
        favorito = "★" if c["favorito"] else " "
        print(f"{i + 1}. [{favorito}] Nome: {c['nome']} - Telefone: {c['telefone']} - Email: {c['email']}")

def atualizar():
    if contato == []:
        print("Nenhum contato encontrado.")
        return

    listar()
    indice = int(input("Digite o número do contato que deseja atualizar: ")) - 1

    if 0 <= indice < len(contato):
        novo_nome = input("Digite o novo nome do contato: ")
        novo_telefone = input("Digite o novo telefone do contato: ")
        novo_email = input("Digite o novo email do contato: ")
        contato[indice]["nome"] = novo_nome
        contato[indice]["telefone"] = novo_telefone
        contato[indice]["email"] = novo_email
        print("Contato atualizado com sucesso!")
    else:
        print("Índice inválido.")

def deletar():
    if contato == []:
        print("Nenhum contato encontrado.")
        return

    listar()
    indice = int(input("Digite o número do contato que deseja deletar: ")) - 1

    if 0 <= indice < len(contato):
        contato_deletado = contato.pop(indice)
        print(f"Contato '{contato_deletado['nome']}' deletado com sucesso!")
    else:
        print("Índice inválido.")

def favoritar():
    if contato == []:
        print("Nenhum contato encontrado.")
        return

    listar()
    indice = int(input("Digite o número do contato que deseja marcar como favorito: ")) - 1

    if 0 <= indice < len(contato):
        contato[indice]["favorito"] = True
        print(f"Contato '{contato[indice]['nome']}' marcado como favorito!")
    else:
        print("Índice inválido.")

def ver_favoritos():
    # [ o_que_vai_entrar_na_lista  for item in lista  if condição ]
    favoritos = [c for c in contato if c["favorito"]]
    if favoritos == []:
        print("Nenhum contato favorito encontrado.")
        return

    print("Contatos favoritos:")
    for i, c in enumerate(favoritos):
        print(f"{i + 1}. Nome: {c['nome']} - Telefone: {c['telefone']} - Email: {c['email']}")

while True:
    print("agenda de contatos")
    print("1. adicionar contato")
    print("2. listar contatos")
    print("3. atualizar contato")
    print("4. deletar contato")
    print("5. marcar contato como favorito")
    print("6. ver contatos favoritos")
    print("7. sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        adicionar(nome, telefone, email)
    elif escolha == "2":
        listar()
    elif escolha == "3":
        atualizar()
    elif escolha == "4":
        deletar()
    elif escolha == "5":
        favoritar()
    elif escolha == "6":
        ver_favoritos()
    elif escolha == "7":
        print("Saindo da agenda de contatos...")
        break
    