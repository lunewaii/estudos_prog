lista = [1, 2, 3, 4, 5]

# métodos de lista
lista[:6]  # retorna os elementos do índice 0 ao 5
lista[2:]  # retorna os elementos do índice 2 até o final
lista.append(6)  # adiciona o elemento 6 ao final da lista
lista.insert(2, 10)  # insere o elemento 10 no índice 2
lista.remove(3)  # remove o elemento 3 da lista, a primeira ocorrência encontrada
lista.pop()  # remove o último elemento da lista
lista.sort()  # ordena a lista em ordem crescente
lista.reverse()  # inverte a ordem dos elementos da lista
lista.clear()  # remove todos os elementos da lista
lista.count(2)  # retorna o número de ocorrências do elemento 2 na lista
lista.index(4)  # retorna o índice do elemento 4 na lista
lista.copy()  # retorna uma cópia da lista
lista.extend([7, 8, 9])  # adiciona os elementos 7, 8 e 9 ao final da lista