//construir um objeto com function era uma gambiarra, porque não tínhamos classes
//com classes, podemos fazer:
class Pessoa {
    constructor(nome, idade, sexo) {
        this.nome = nome;
        this.idade = idade;
        this.sexo = sexo;
    }

    falaNome() {
        return this.nome;
    }
}

let pessoa = new Pessoa('Ana', 50, 'F');
//retorna ana:
console.log(pessoa.falaNome());

class Personagem extends Pessoa{
    constructor(nome, idade, sexo, classe){
        super(nome, idade, sexo); //preciso disso sempre pra declarar o que foi herdado
        this.classe = classe;
    }
}

let personagem = new Personagem('dva', 19, 'F', 'tanque');
//retorna tanque:
console.log(personagem.classe);