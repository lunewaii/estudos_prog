//como abrir um servidor http usando node
//pega um modulo http que ja vem no node
var http = require('http');

const server = http.createServer(function (req, res) { 
  res.end('Hello World!'); //end -> fecha a conexao e conclui a resposta
})

server.listen(8080); //escuta na porta 8080

console.log('servidor rodando na porta ' + server.address().port); //mostra a porta que o servidor esta rodando