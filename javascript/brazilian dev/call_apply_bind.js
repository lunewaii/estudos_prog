//bind redefine o contexto (this) da função
const pessoa = {
    nome: "João",
    saudacao: function() {
      console.log(`Olá, meu nome é ${this.nome}`);
    }
  };
  
  const outraPessoa = {
    nome: "Maria"
  };
  
  // Usando bind para criar uma nova função com 'this' definido como 'outraPessoa'
  const saudacaoDeMaria = pessoa.saudacao.bind(outraPessoa);
  
  saudacaoDeMaria(); // Saída: "Olá, meu nome é Maria"

// diferença entre call e apply:
// call recebe os argumentos separados por vírgula
// apply recebe os argumentos em um array

//call
const obj1 = {
    exemplo1: "exemplo1",
    mostraThis: function() {
        console.log(this);
    }
}

const obj2 = {
    exemplo2: "exemplo2"
}

obj1.mostraThis.call(obj2); 