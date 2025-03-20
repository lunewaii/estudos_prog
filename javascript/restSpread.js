//spread
var nomes = [
    {
        nome: 'gabs'
    },
    {
        nome: 'rebs'
    }
]


//com esse spread (...nomes) eu adiociono os objetos de nomes em obj
const obj = [...nomes,{
    nome: 'garebs'
}]

//rest
function testes(...numeros){
    console.log(numeros);
}

testes(1,2,3,4,5,6,7,8,9,10);