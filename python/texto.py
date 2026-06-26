#rebeca carneiro
nome_normal = "rebeca carneiro"
#rebeca
#carneiro
#paula
nome_separado = """rebeca
carneiro
paula"""

#esse transforma em string antes de mostrar
print("nome normal: %s, nome separado: %s" % (nome_normal, nome_separado))

#esse nao transforma
print(f"nome normal: {nome_normal}, nome separado: {nome_separado}")

#outra forma
print("nome normal: {}, nome separado: {}".format(nome_normal, nome_separado))

print("-".join(nome_separado)) #junta tudo com o que eu colocar no join

print(nome_normal.split()) #separa em lista, por padrão separa por espaço