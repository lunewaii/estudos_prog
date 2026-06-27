class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    #essa função usa cls (class) porque precisa acessar dados da classe
    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, int(ano))
    
configuracao1 = "Toyota,Corolla,2020"
carro1 = Carro.criar_carro(configuracao1)
print(f"Carro 1 \nmarca: {carro1.marca}, modelo: {carro1.modelo}, ano: {carro1.ano}")

class Matematica:
    # essa função não precisa de self, porque ela não depende de nenhum atributo da classe
    @staticmethod
    def somar(a, b):
        return a + b
    
print(f"Soma: {Matematica.somar(5, 3)}")
