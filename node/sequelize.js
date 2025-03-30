const Sequelize = require('sequelize');
const sequelize = new Sequelize('sistemaCadastro', 'root', 'lun3w411', {
    host: 'localhost',
    dialect: 'mysql'
})

sequelize.authenticate().then(() => {
    console.log('conectado ao banco de dados')
}).catch((err)=>{
    console.log('não foi possível conectar: ' + err)
})