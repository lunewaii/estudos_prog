const express = require('express');
const app = express();

app.get("/", function(req, res){
    res.send('pagina carregada com sucesso!');
});

//so posso mandar o send uma vez!
//o ? deixa o parametro como opcional
app.get("/oi/:nome?", function(req, res){
    const nome = req.params.nome; //pega o parametro da url
    res.send('Oi ' + nome + ' :)');
})


app.listen(3000, function(){
    console.log('Servidor rodando');
})