# herança, polimorfismo e encapsulamento
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def andar(self):
        print(f"{self.nome} está andando.")

    def emitir_som(self):
        pass  # Método a ser implementado pelas subclasses

class Cachorro(Animal):
    def emitir_som(self):
        return "Au au!"
    
class Gato(Animal):
    def emitir_som(self):
        return "Miau!"
    
dog = Cachorro("Rex")
cat = Gato("Whiskers")

# exemplo de polimorfismo
animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")

# exemplo de encapsulamento
class ContaBancaria:
    def __init__(self, saldo=0):
        self.__saldo = saldo  # atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de {valor} realizado. Saldo atual: {self.__saldo}")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de {valor} realizado. Saldo atual: {self.__saldo}")
        else:
            print("Saldo insuficiente ou valor inválido.")
    
    def consultar_saldo(self):
        return self.__saldo
    
conta = ContaBancaria(saldo=1000)
print(f"Saldo inicial: {conta.consultar_saldo()}")
conta.depositar(500)
conta.sacar(200)
print(f"Saldo final: {conta.consultar_saldo()}")

# abstração
from abc import ABC, abstractmethod
# classe abstrata é só um molde, não pode ser instanciada diretamente
class Veiculo(ABC):
    # usar esse abstract faz com que os "filhos" da classe abstrata sejam 
    # obrigados a implementar esses métodos
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):
    def ligar(self):
        print("O carro está ligado.")

    def desligar(self):
        print("O carro está desligado.")

carro = Carro()
carro.ligar()
carro.desligar()