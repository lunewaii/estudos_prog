fetch('https://jsonplaceholder.typicode.com/todos/1',{
    method:'POST',
    body: JSON.stringify({
        title: 'quartz',
        body: 'conteúdo',
        userId: 3
    }),
    headers:{
        'Content-Type': 'application/json; charset=UTF-8'
    }
})
.then(response => response.json())
.then(json => console.log(json))
//a resposta é a mesma do que usa XML, mas vou aprender depois a usar os status
