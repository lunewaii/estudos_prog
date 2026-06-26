numeros = {"pares": [2, 4, 6, 8], "impares": [1, 3, 5, 7]}

# métodos: keys(), values(), items()
chaves = numeros.keys()
print("chaves do dicionario:", chaves)
# caso eu queira acessar uma chave pelo indice, posso converter para uma lista
chaves_lista = list(chaves)
print("primeira chave do dicionario:", chaves_lista[0])

valores = list(numeros.values())
print("valores do dicionario:", valores)

itens = list(numeros.items())
print("chave-valor do dicionario:", itens)   #cada conjunto vira uma tupla
