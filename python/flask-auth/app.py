from flask import Flask, request, jsonify
from models.user import User
from database import db
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username and password:
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            return jsonify({'message': 'Sucesso no login'}), 200
    else:
        return jsonify({'message': 'Credenciais inválidas'}), 401

@app.route('/hi', methods=['GET'])
def hi():
    return jsonify({'message': 'hello, world!>:)'})

if __name__ == '__main__':
    app.run(debug=True)