
from flask import Flask, jsonify
from src.apis.user import blueprint as user


app = Flask(__name__)

app.register_blueprint(user)

@app.route('/')
def welcome():
    info = ['Flask Api']
    return '\n'.join(info)


if __name__ == '__main__':
    app.run(debug=True)