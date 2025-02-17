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

//call muda o metodo de um objeto
const obj1 = {
    exemplo1: "exemplo1",
    mostraThis: function() {
        console.log(this);
    }
}

obj1.mostraThis()

const obj2 = {
    exemplo2: "exemplo2"
}

obj1.mostraThis.call(obj2);

//apply muda o metodo de um objeto
const obj3 = {
    exemplo3: "exemplo3",
    mostraThis: function() {
        console.log(this);
    }
}

obj3.mostraThis()

const obj4 = {
    exemplo4: "exemplo4"
}

obj3.mostraThis.apply(obj4);