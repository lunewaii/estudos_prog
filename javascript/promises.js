function promise(){
    return new Promise((resolve, reject) => {
        const erro = true;
        if(erro){
            reject('Erro: Ocorreu um erro');
        } else {
            resolve('Sucesso: Promessa resolvida');
        }
    });
}

promise()
    .then((res)=>{
        console.log(res);
    })
    .catch((err)=>{
        console.log(err);
    })

    //uma forma melhor de usar é com async e await