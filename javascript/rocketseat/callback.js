
//um callback é uma funçao passada como paramento para outra função
//exemplo:
function saudacao(nome) {
    console.log('Olá, ' + nome);
}

function processaEntradaUsuario(callback) {
    var nome = 'Maria';
    callback(nome);
}

processaEntradaUsuario(saudacao);
