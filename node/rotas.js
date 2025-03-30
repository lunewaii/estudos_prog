const express = require('express'); //retorna uma funçao que cria um servidor
const app = express(); //recebe a funcao express que cria o servidor

//funcao de callback é uma funcao que acontece quando um evento acontece

app.get("/", function(req,res){
    res.send('mensagem enviada para o cliente');
});

app.get("/ola", function(req,res){
    res.send('Ola mundo!'); //resposta para o cliente
});


const server = app.listen(8080, function(){
    const port = server.address().port; //pega a porta que o servidor esta rodando
    console.log('Servidor rodando na porta ' + port); //imprime no console a porta que o servidor esta rodando
}); //TEM QUE SER A ULTIMA LINHA DO ARQUIVO