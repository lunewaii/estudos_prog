var agora = new Date()
var diaSem = agora.getDay()

switch(diaSem){
    case 0:
        console.log('hoje é domingo')
        break
    case 1:
        console.log('hoje é segunda')
        break
    case 2:
        console.log('hoje é terça')
        break
    case 3:
        console.log('hoje é quarta')
        break
    case 4:
        console.log('hoje é quinta')
        break
    case 5:
        console.log('hoje é sexta')
        break
    case 6:
        console.log('hoje é sabado')
        break
    default: //no caso de nao ser nenhum dos outros, caso eu tenha definido um dia pra variavel
        console.log('hoje é um dia da semana rs')
    }