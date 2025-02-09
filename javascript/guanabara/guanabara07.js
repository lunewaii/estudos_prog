let val = [5, 8, 2, 9, 3]
val.push(1) //coloca 1 no final
val.sort() //poe em ordem crescente
console.log(val)

for(let pos in val){ //vai repetindo pra quantos valores tiver em val
    console.log(`a posição ${pos} tem o valor ${val[pos]}!`)
}
var oito = val.indexOf(8)
console.log(`O 8 está na posição ${oito}`)