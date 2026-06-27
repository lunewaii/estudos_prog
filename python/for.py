numeros = {"pares": [2, 4, 6, 8], "impares": [1, 3, 5, 7]}
print ("for usando dicionario - chaves")
for chave in numeros.keys():
    print(chave)

print ("for usando dicionario - valores")
for valor in numeros.values():
    print(valor)

print ("for usando dicionario - itens")
for chave, valor in numeros.items():
    print(f"{chave}: {valor}")

# range(): intervalo numérico
print("for usando range()")
for i in range(5):
    print(i)

print("range com len(numeros)")
for i in range(len(numeros)):
    print(i)

# dá certo porque o enumerate() retorna dois valores: índice e valor
enumerate = ["maçã", "banana", "laranja"]
for i, fruta in enumerate(enumerate):
    print(f"{i}: {fruta}")