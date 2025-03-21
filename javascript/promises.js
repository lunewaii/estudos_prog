console.log('oi');

function promise(){
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const erro = true;
            if(erro){
                reject('Erro: Ocorreu um erro');
            } else {
                resolve('Sucesso: Promessa resolvida');
            }
        }, 5000);
    });
}

// promise()
//     .then((res)=>{
//         console.log(res);
//     })
//     .catch((err)=>{
//         console.log(err);
//     })

//uma forma melhor de usar é com async e await

async function teste(){
    await promise().then((res)=>{
        console.log(res);
        })
        .catch((err)=>{
        console.log(err);
        });
    console.log('resolvido depois da promise');
}

teste();