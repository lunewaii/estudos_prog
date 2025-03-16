//formas de inserir e remover elementos de um array em js
//inserindo elementos no array
const arr = [1, 2, 3];
console.log(arr);

//coloca o elemento no final do array
arr.push(4);
console.log(arr);

//coloca o elemento no início do array
arr.unshift(0);
console.log(arr);

//coloca o elemento no meio do array
//adiciona 1.5 no índice 2 sem remover elementos
arr.splice(2, 0, 1.5);
console.log(arr);

//removendo elementos do array
//remove o último elemento do array
arr.pop();
console.log(arr);

//remove o primeiro elemento do array
arr.shift();
console.log(arr);

//remove o elemento do meio do array
//remove 1 elemento a partir do índice 2
arr.splice(2, 1);
console.log(arr);

//removendo todos os elementos a partir do índice 1
arr.splice(2);
console.log(arr);