//declaração clássica de função
function soma(a, b) {
    var sum = a + b;
    return sum;
}

console.log(soma(2, 3)); // 5

//declaração de função anônima
var soma = function(a, b) {
    return a + b;
}

console.log(soma(2, 3)); // 5

//declaração de função anônima com arrow function
var soma = (a, b) => a + b;