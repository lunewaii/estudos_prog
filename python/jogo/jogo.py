# personagem: classe mae
# heroi: controlado pelo usuario
# inimigo: adversario do usuario
import random

class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"\n-----------------------\nnome: {self.get_nome()} \nVida: {self.get_vida()}\nNível: {self.get_nivel()}"

    def receber_ataque(self, dano):
        self.__vida -= dano

    def atacar(self, alvo):
        dano = random.randint(2, self.get_nivel() * 2)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")


class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade
    
    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}"
    
    def especial(self, alvo):
        dano = random.randint(5, self.get_nivel() * 5)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} usou a habiliadde especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano!")
    
class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}\n-----------------------"
    
class Jogo:
    """  classe orquestradora do jogo """

    def __init__(self):
        self.heroi = Heroi("gabriel", 100, 5, "amor")
        self.inimigo = Inimigo("morcegao", 80, 5, "psíquico")

    def iniciar_batalha(self):
        """  mecanismo de batalha """
        print("iniciando batalha")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("detalhes dos personagens:")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("pressione enter para atacar!")
            escolha = input("1 - ataque normal, 2 - ataque especial. Escolha: ")

            if escolha == '1':
                self.heroi.atacar(self.inimigo)
            elif escolha == '2':
                self.heroi.especial(self.inimigo)
            else:
                print("escolha inválida, tente novamente")

            if self.inimigo.get_vida() > 0:
                self.inimigo.atacar(self.heroi)

        if self.heroi.get_vida() <= 0:
            print("A sua vida acabou. Jogo finalizado :(")

        if self.inimigo.get_vida() <= 0:
            print("A vida do inimigo acabou. Jogo finalizado :)")

# criar instancia do jogo e começar a batalha
jogo = Jogo()
jogo.iniciar_batalha()
        