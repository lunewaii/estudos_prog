//mandando o html para o front
const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/html/index.html');
});

app.listen(3000, () => {
    console.log('servidor rodando!');
})