print("exemplo de captura de exceções")

while True:
    try:
        numero = int(input("digite um número: "))
        print(f"seu número dividido por 2 é: {numero / 2}")
    except ValueError:
        print("Por favor, digite um número válido.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        print("Programa finalizado.")