//aqui a const 'obj' está sendo copiada para a const 'copia' com o método Object.assign
//o método Object.assign é usado para copiar um objeto para outro, 
// ele recebe dois parâmetros, o primeiro é o objeto que 
// será copiado e o segundo é o objeto que receberá a cópia
const obj1 = {a: 1}
const copia = Object.assign({}, obj)

//mescla todos eles em um objeto só
const o1 = {a: 1};
const o2 = {b: 2};
const o3 = {c: 3};

const obj2 = Object.assign({}, o1, o2, o3);

