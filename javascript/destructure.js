//destructure
const arr = ['rebs', 'gabs', 'garebs', 'dva', 'viper'];
const [a, b, ...c] = arr;

console.log(a); // rebs
console.log(b); // gabs
console.log(c); // ['garebs', 'dva', 'viper']