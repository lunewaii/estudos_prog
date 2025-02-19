//funções de primeira classe em js
function printa(){
    return () => console.log('oi');
}

//formas de chamar a funcção:
//parênteses duplo
printa()();

//atribuindo a função a uma variável
const chamar2 = printa();
chamar2();