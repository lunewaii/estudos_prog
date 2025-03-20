
//um callback é uma funçao passada como paramento para outra função
//exemplo:
function saudacao(nome) {
    console.log('Olá, ' + nome);
}

function processaEntradaUsuario(x) {
    var nome = 'Maria';
    x(nome);
}

processaEntradaUsuario(saudacao);
