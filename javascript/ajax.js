///////////// receita de bolo pra usar ajax
var req = new XMLHttpRequest();
req.open('GET','https://jsonplaceholder.typicode.com/todos/1','true'); //diz que o metodo é get, fala a url e true sobre ser assincrono

req.onload = function() {
    if(this.status >= 200 && this.status < 400){
        //request feita com sucesso
        let data = JSON.parse(this.response);
        console.log(data);
    } else{ //se a resposta foi um erro
        console.log('error')
    }
}

req.onerror = function(){
    console.log('ocorreu um erro e a requisiçao nao pode ser feita');
}

req.send();
///////////