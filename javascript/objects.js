//objetos podem ser criados de três formas:
//1. Usando um construtor de objeto
//2. Usando um objeto literal
//3. Usando um construtor de função
//exemplos:
//1. Usando um construtor de objeto
let pessoa = new Object();
pessoa.nome = 'João';
pessoa.idade = 20;
pessoa.sexo = 'M';
//2. Usando um objeto literal
let pessoa2 = {
    nome: 'Maria',
    idade: 30,
    sexo: 'F'
};
//3. Usando um construtor de função
function Pessoa(nome, idade, sexo) {
    this.nome = nome;
    this.idade = idade;
    this.sexo = sexo;
}
let pessoa3 = new Pessoa('José', 40, 'M');
console.log(pessoa3);