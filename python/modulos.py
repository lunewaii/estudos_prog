print("exemplo de importação de um módulo padrão")

# import math
from math import sqrt

numero = float(input("digite um número: "))
raiz_quadrada = sqrt(numero)
print(f"A raiz quadrada de {numero} é {raiz_quadrada:.2f}")

print("exemplo de criação e utilização de um módulo personalizado")

import meu_modulo
nome = input("Digite seu nome: ")
print(meu_modulo.saudacao(nome))

a = float(input("digite o primeiro número: "))
b = float(input("digite o segundo número: "))
print(f"A soma de {a} e {b} é: {meu_modulo.soma(a, b)}")
print(f"A subtração de {a} e {b} é: {meu_modulo.subtracao(a, b)}")
print(f"A multiplicação de {a} e {b} é: {meu_modulo.multiplicacao(a, b)}")