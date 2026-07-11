from flask import Flask
from models.user import User
from database import db
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db.init_app(app)

@app.route('/hi', methods=['GET'])
def hi():
    return 'hello, world! >:)'

if __name__ == '__main__':
    app.run(debug=True)